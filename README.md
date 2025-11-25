# Insta-Collect: Modular Instagram Data Collector

## Project Status: In Development

This project is currently under active development. The core functionality for hashtag photo scraping is stable, but features for collecting comments, user data, and managing large-scale video/Reel scraping are planned for future releases.

***

## Project Overview

Insta-Collect is a simple, modular Python project utilizing **Playwright** for web automation and data extraction from Instagram. The goal is to provide a versatile tool for collecting structured data for analysis and research purposes.

The current focus is on building a robust method for retrieving photo-based posts via hashtags.

***

## Current Key Features (v1.0)

* **Hashtag Scraping:** Core functionality for targeted data collection based on hashtags.
* **Accurate Data Capture:** Collects **Caption**, **Username**, **Timestamp**, and **Post URL**.
* **Content Filtering:** Automatically excludes Video and Reels content to maintain data consistency in photo-focused outputs.
* **Session Management:** Supports using a `cookies.json` file to bypass the Instagram Login Wall and mitigate rate limits.
* **Output:** Saves results to structured **JSON** files.

***

## Future Plans (Roadmap)

We plan to expand the capabilities of Insta-Collect to include:

* **Comment Scraping:** Retrieving all comments associated with a scraped post.
* **User Profile Data:** Collecting biographical information and post metadata from specific user profiles.
* **Video/Reel Support:** Implementing a separate, more complex logic to handle video-based content.
* **CSV Output:** Adding an option to save data in CSV format.

***
##  Setup and Installation

1. **Clone Repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/insta-collect.git
    cd insta-collect
    ```

2. **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Make sure `requirements.txt` contains `playwright` and `argparse`)*

3. **Install Playwright Browser:**
    ```bash
    playwright install
    ```

4. **Prepare Cookies (Important!):**
    To avoid getting blocked (`null` data) when visiting many posts, you **must** use a logged-in session.
    * Save the cookie file from your logged-in Instagram browser session into `cookies.json` in the root directory.
    * **Warning:** Add this file to `.gitignore` so your credentials are not uploaded to GitHub!

##  How to Run the Scraper

| Argument | Description | Required? | Example |
| :--- | :--- | :--- | :--- |
| `--tag` | The hashtag to scrape (without `#`). | Yes | `jokowi` |
| `--limit` | Number of PHOTO posts to scrape. | No (Default: 10) | `50` |
| `--cookie` | Path to `cookies.json`. **Highly recommended.** | No | `cookies.json` |

### Example Usage

**Scraping Photo posts with Cookies:**
```bash
python cli.py --tag jokowi --limit 5 --cookie cookies.json
```

```json
[
  {
    "url": "[https://www.instagram.com/p/DLOvv7tP4ra/](https://www.instagram.com/p/DLOvv7tP4ra/)",
    "caption": "@jokowi baru-baru ini diduga mengalami alergi kulit setelah kunjungan ke Vatikan... [Dipotong untuk kerapian]",
    "username": null,
    "timestamp": "2025-06-23T04:46:39.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "[https://www.instagram.com/p/DRdp_HDkjxI/](https://www.instagram.com/p/DRdp_HDkjxI/)",
    "caption": null,
    "username": null,
    "timestamp": null,
    "source_tag": "jokowi"
  },
  {
    "url": "[https://www.instagram.com/p/DRb8qWjjCBf/](https://www.instagram.com/p/DRb8qWjjCBf/)",
    "caption": "@jokowi baru-baru ini diduga mengalami alergi kulit setelah kunjungan ke Vatikan... [Dipotong untuk kerapian]",
    "username": null,
    "timestamp": null,
    "source_tag": "jokowi"
  },
  {
    "url": "[https://www.instagram.com/p/DFMPnM5SJ0r/](https://www.instagram.com/p/DFMPnM5SJ0r/)",
    "caption": "@jokowi baru-baru ini diduga mengalami alergi kulit setelah kunjungan ke Vatikan... [Dipotong untuk kerapian]",
    "username": null,
    "timestamp": null,
    "source_tag": "jokowi"
  },
  {
    "url": "[https://www.instagram.com/p/DRdrw5HkkJB/](https://www.instagram.com/p/DRdrw5HkkJB/)",
    "caption": "Tapanuli Selatan di Bawah Langit yang Menangis: Jalan Amblas, Sungai Mengganas... [Dipotong untuk kerapian]",
    "username": null,
    "timestamp": "2025-11-25T03:08:48.000Z",
    "source_tag": "jokowi"
  }
]



```
