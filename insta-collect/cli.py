import argparse
import sys
import os
from src.saver import save_data 


sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


from src.scraper import scrape_hashtag

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", required=True)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--cookie", help="Path to cookies.json", default=None)

    args = parser.parse_args()


    cookies_path = args.cookie
    if cookies_path and not os.path.exists(cookies_path):
        print(f"[WARNING] File {cookies_path} tidak ditemukan! Menjalankan tanpa login...")
        cookies_path = None

    print(f"[*] Target: #{args.tag} | Limit: {args.limit}")

    data = scrape_hashtag(
        hashtag=args.tag,
        limit=args.limit,
        cookies_file=cookies_path
    )

    print(f"[DONE] Mendapatkan {len(data)} data.")
    
    if data:
        save_data(data, filename=f"hasil_{args.tag}")

if __name__ == "__main__":
    main()
