#!/usr/bin/env python3
"""串行下载已开页面取得的完整小红书 CDN URL；文件编号不表示原图序。"""
import argparse
import http.client
import json
import os
from pathlib import Path
import re
import sys
import time
from urllib.parse import urlsplit


def image_type(data):
    if data.startswith(b'\xff\xd8\xff'):
        return 'jpeg', '.jpg'
    if data.startswith(b'\x89PNG\r\n\x1a\n'):
        return 'png', '.png'
    if data[:6] in (b'GIF87a', b'GIF89a'):
        return 'gif', '.gif'
    if data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        return 'webp', '.webp'
    raise ValueError('响应内容不是 JPEG、PNG、WebP 或 GIF')


def image_url(raw):
    if not isinstance(raw, str) or any(c.isspace() or ord(c) < 32 for c in raw):
        raise ValueError('image_urls 必须为完整 HTTP/HTTPS CDN 字符串列表')
    parsed = urlsplit(raw)
    host = parsed.hostname or ''
    if (parsed.scheme not in ('http', 'https') or not host.endswith('.xhscdn.com')
            or host == '.xhscdn.com' or parsed.username is not None
            or parsed.password is not None
            or (parsed.scheme == 'http' and parsed.port is not None)
            or (parsed.scheme == 'https' and parsed.port not in (None, 443))
            or parsed.fragment or not parsed.path):
        raise ValueError('图片 URL 必须为 HTTP/HTTPS *.xhscdn.com，无认证或片段；HTTP 不带端口，HTTPS 仅允许 443')
    return parsed


def download(url, destination, limit):
    parsed = image_url(url)
    if parsed.scheme != 'https':
        raise ValueError('实际下载仅允许 HTTPS')
    connection = http.client.HTTPSConnection(parsed.hostname, parsed.port or 443, timeout=20)
    deadline = time.monotonic() + 20
    response = None
    try:
        target = parsed.path + ('?' + parsed.query if '?' in url else '')
        connection.request('GET', target, headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'image/*'})
        connection.sock.settimeout(max(0.001, deadline - time.monotonic()))
        response = connection.getresponse()
        if not 200 <= response.status < 300:
            raise ValueError('HTTP %s（不跟随重定向，不重试）' % response.status)
        content_type = response.getheader('Content-Type', '').split(';', 1)[0].strip().lower()
        if not content_type.startswith('image/'):
            raise ValueError('响应 Content-Type 不是 image/*')
        length = response.getheader('Content-Length')
        if length is not None and int(length) > limit:
            raise ValueError('响应超出剩余总字节预算')
        # HTTPConnection 在 Connection: close 时移交 socket 给响应对象。
        response_socket = connection.sock or response.fp.raw._sock
        size = 0
        prefix = b''
        with destination.open('xb') as output:
            while True:
                remaining_time = deadline - time.monotonic()
                if remaining_time <= 0:
                    raise TimeoutError('下载超过 20 秒')
                response_socket.settimeout(remaining_time)
                chunk = response.read1(min(65536, limit - size + 1))
                if not chunk:
                    break
                size += len(chunk)
                if size > limit:
                    raise ValueError('响应超出剩余总字节预算')
                if len(prefix) < 12:
                    prefix = (prefix + chunk)[:12]
                output.write(chunk)
        if length is not None and size != int(length):
            raise ValueError('响应长度与 Content-Length 不一致')
        kind, extension = image_type(prefix)
        final = destination.with_suffix(extension)
        destination.rename(final)
        return final.name, kind, size
    finally:
        if response is not None:
            response.close()
        connection.close()
        if destination.exists():
            destination.unlink()


def main(argv=None):
    os.umask(0o077)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    parser.add_argument('--max-images', type=int, default=6)
    parser.add_argument('--max-bytes', type=int, default=20 * 1024 * 1024)
    args = parser.parse_args(argv)
    if not 1 <= args.max_images <= 20 or args.max_bytes < 1:
        parser.error('--max-images 必须在 1–20，--max-bytes 必须为正整数')
    try:
        data = json.loads(args.input.read_text(encoding='utf-8'))
        if not isinstance(data, dict) or not isinstance(data.get('url'), str):
            raise ValueError('输入必须包含规范 url 与 image_urls')
        if not re.fullmatch(r'https://www\.xiaohongshu\.com/explore/[a-fA-F0-9]{6,80}', data['url']):
            raise ValueError('url 必须为已核实的规范小红书笔记链接')
        urls = data.get('image_urls')
        if not isinstance(urls, list):
            raise ValueError('image_urls 必须为列表')
        for url in urls:
            image_url(url)
        unique = list(dict.fromkeys(urls))
        args.output_dir.mkdir(mode=0o700)
    except (OSError, ValueError, TypeError) as error:
        parser.error(str(error))
    result = {'url': data['url'], 'discovered_count': len(urls),
              'unique_count': len(unique), 'downloaded_count': 0,
              'undownloaded_count': len(unique), 'images': [], 'failure': None}
    total = 0
    for index, url in enumerate(unique[:args.max_images], 1):
        local_id = 'image-%02d' % index
        # 只替换 scheme，保留 CDN 主机、路径、query 与 ! 样式。
        download_url = 'https:' + url.partition(':')[2] if image_url(url).scheme == 'http' else url
        try:
            if total >= args.max_bytes:
                raise ValueError('总字节预算已耗尽')
            filename, kind, size = download(download_url, args.output_dir / (local_id + '.part'), args.max_bytes - total)
        except (OSError, ValueError, http.client.HTTPException) as error:
            result['failure'] = {'local_id': local_id, 'source_url': url, 'download_url': download_url,
                                 'error': str(error)}
            break
        total += size
        result['images'].append({'local_id': local_id, 'file': filename, 'source_url': url, 'download_url': download_url,
                                 'source_index': None, 'type': kind, 'bytes': size})
    result['downloaded_count'] = len(result['images'])
    result['undownloaded_count'] = len(unique) - result['downloaded_count']
    result['total_bytes'] = total
    (args.output_dir / 'images.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('下载 %s/%s 张；未下载 %s 张；%s' % (result['downloaded_count'], len(unique), result['undownloaded_count'], '失败，见 images.json' if result['failure'] else '完成'))
    return 1 if result['failure'] else 0


if __name__ == '__main__':
    sys.exit(main())
