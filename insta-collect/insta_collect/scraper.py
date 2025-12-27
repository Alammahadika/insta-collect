from playwright.sync_api import sync_playwright
import json
import time
import random
import re


# ================= UTIL =================
def count_sentences(text):
    if not text:
        return 0
    sentences = re.split(r"[.!?]+", text)
    return len([s for s in sentences if s.strip()])


# ================= DETAIL SCRAPER =================
def get_post_details(page, url):
    """
    Ambil detail post Instagram
    Fokus: caption teks (meta -> DOM)
    """
    data = {
        "caption": None,
        "caption_status": None,
        "timestamp": None,
        "is_video": False
    }

    try:
        print(f"   [..] Visiting: {url}")
        page.goto(url, wait_until="load", timeout=15000)

        if "login" in page.url:
            data["caption_status"] = "redirect_login"
            return data

        try:
            page.wait_for_selector("article span, article h1", timeout=6000)
        except:
            pass

        caption_text = None

        # ---------- META (PALING STABIL) ----------
        try:
            meta_desc = page.locator(
                'meta[property="og:description"]'
            ).get_attribute("content")

            if meta_desc and ": " in meta_desc:
                caption_text = meta_desc.split(": ", 1)[1].strip().strip('"')
        except:
            pass

        # ---------- DOM FALLBACK ----------
        if not caption_text:
            try:
                candidates = page.locator("article span").all()
                longest_text = None

                for el in candidates:
                    try:
                        text = el.inner_text().strip()
                        if not text:
                            continue
                        if len(text) < 100:
                            continue
                        if text.lower() in [
                            "like", "reply", "see translation",
                            "more", "following", "follow"
                        ]:
                            continue

                        if not longest_text or len(text) > len(longest_text):
                            longest_text = text
                    except:
                        continue

                caption_text = longest_text
            except:
                pass

        # ---------- VALIDASI KALIMAT ----------
        sentence_count = count_sentences(caption_text)

        if not caption_text or sentence_count < 2:
            data["caption"] = None
            data["caption_status"] = "no_text"

        elif sentence_count < 8:
            data["caption"] = caption_text
            data["caption_status"] = "short_text"

        else:
            data["caption"] = caption_text
            data["caption_status"] = "long_text"

        # ---------- TIMESTAMP ----------
        try:
            time_el = page.locator("time").first
            if time_el.count() > 0:
                data["timestamp"] = time_el.get_attribute("datetime")
        except:
            pass

        # ---------- VIDEO FLAG ----------
        try:
            if page.locator("video").count() > 0:
                data["is_video"] = True
        except:
            pass

    except Exception as e:
        data["caption_status"] = "error"
        print(f"   [!] Error scraping detail: {e}")

    return data


# ================= HASHTAG SCRAPER =================
def scrape_hashtag(hashtag, limit=10, cookies_file=None):
    photo_results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        if cookies_file:
            try:
                with open(cookies_file, "r") as f:
                    context.add_cookies(json.load(f))
                    print("[INFO] Cookies loaded")
            except:
                pass

        page = context.new_page()

        # ---------- SCAN HASHTAG ----------
        print(f"[1/3] Scanning hashtag #{hashtag}")
        tag_url = f"https://www.instagram.com/explore/tags/{hashtag}/"
        page.goto(tag_url, wait_until="domcontentloaded")
        time.sleep(3)

        collected_links = set()

        while len(collected_links) < limit * 2:
            nodes = page.locator("a[href*='/p/']").all()
            for node in nodes:
                href = node.get_attribute("href")
                if href:
                    collected_links.add(f"https://www.instagram.com{href}")
                if len(collected_links) >= limit * 2:
                    break

            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1.5)

        print(f"[INFO] Found {len(collected_links)} links")

        # ---------- SCRAPE DETAIL (EARLY STOP) ----------
        print("[2/3] Scraping detail posts")
        for i, link in enumerate(collected_links):
            if len(photo_results) >= limit:
                print("[INFO] Limit reached. Stop scraping.")
                break

            print(f"   -> {i+1}/{len(collected_links)}")
            details = get_post_details(page, link)

            if details["is_video"]:
                continue

            photo_results.append({
                "url": link,
                "caption": details["caption"],
                "caption_status": details["caption_status"],
                "timestamp": details["timestamp"],
                "source_tag": hashtag
            })

            time.sleep(random.uniform(1, 2))

        browser.close()

    print(f"[DONE] Collected {len(photo_results)} posts")
    return photo_results
