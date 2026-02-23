from bs4 import BeautifulSoup
import re


def parse_instagram_html(file_path, min_len=10):

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    results = []
    current_user = None
    caption_done = False

    UI_TEXTS = {
        "Instagram Lite",
        "Log in",
        "Sign up",
        "Open in app",
        "Reply",
        "Like",
        "See translation",
        "View all replies",
        "View replies",
        "More",
        "Follow",
        "Suggested for you"
    }

    def is_username(text):
        return (
            text.islower()
            and " " not in text
            and 3 <= len(text) <= 30
            and text not in UI_TEXTS
        )

    def is_timestamp(text):
        return re.match(r"^\d+[smhdw]$", text) is not None

    for span in soup.find_all("span"):

        text = span.get_text(strip=True)

        if not text:
            continue

        if text in UI_TEXTS:
            continue

        if is_timestamp(text):
            continue

        if is_username(text):
            current_user = text
            continue

        if current_user and len(text) >= min_len:

            entry_type = "caption" if not caption_done else "comment"
            caption_done = True

            clean_text = re.sub(r"Verified\d+[smhdw]", "", text)

            results.append({
                "username": current_user,
                "text": clean_text,
                "type": entry_type,
                "char_len": len(clean_text)
            })

            current_user = None

    print(f"[DEBUG] Parsed {len(results)} entries")

    return results
  
