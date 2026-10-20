(() => {
  if (location.protocol !== "https:" || location.hostname !== "www.xiaohongshu.com" || (location.port && location.port !== "443")) throw new Error("Not an HTTPS Xiaohongshu page");
  const match = location.pathname.match(/^\/(?:explore|search_result)\/([a-f0-9]+)\/?$/i);
  if (!match) throw new Error("Not a note detail page");
  const noteId = match[1];
  const root = document.querySelector("#noteContainer");
  const title = document.querySelector("#detail-title");
  const desc = document.querySelector("#detail-desc");
  if (!root || !title || !desc) throw new Error("Missing main note DOM");
  const pageText = document.body.innerText;
  if (/安全限制|访问链接异常|验证后继续|登录后查看/.test(pageText)) throw new Error("Page access barrier");
  const unwrap = value => value && value.__v_isRef === true ? value.value : value;
  const state = unwrap(window.__INITIAL_STATE__?.note);
  const map = unwrap(state?.noteDetailMap);
  const entry = unwrap(map?.[noteId]);
  const note = unwrap(entry?.note) || entry;
  const metadataId = unwrap(note?.noteId) || unwrap(note?.id);
  if (metadataId && metadataId !== noteId) throw new Error("Metadata note mismatch");
  const list = unwrap(note?.imageList);
  let imageUrls = Array.isArray(list) ? list.map(item => {
    const image = unwrap(item);
    return unwrap(image?.urlDefault) || unwrap(image?.urlPre) || unwrap(image?.url) || "";
  }).filter(value => typeof value === "string" && value) : [];
  const mediaSource = imageUrls.length ? "matched_note_imageList" : "main_media_DOM";
  if (!imageUrls.length) {
    imageUrls = Array.from(root.querySelectorAll(".swiper-slide img, .carousel-image img, .note-slider img, .note-image img"))
      .map(img => img.currentSrc || img.src || img.getAttribute("data-src")).filter(Boolean);
  }
  if (!title.innerText.trim() && !desc.innerText.trim() && !imageUrls.length) throw new Error("Empty note content");
  const scalar = value => ["string","number"].includes(typeof unwrap(value)) ? unwrap(value) : null;
  return JSON.stringify({url:"https://www.xiaohongshu.com/explore/"+noteId,note_id:noteId,title:title.innerText,body:desc.innerText,text_scope:"browser_visible_body",original_time:scalar(note?.time),edited_time:scalar(note?.lastUpdateTime),image_urls:Array.from(new Set(imageUrls)),media_source:mediaSource,source_index:null,image_count:mediaSource === "matched_note_imageList" ? list.length : null});
})()
