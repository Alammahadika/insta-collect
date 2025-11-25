# insta-collect: Instagram Hashtag Scraper

A simple Python project using Playwright to collect Instagram post data based on hashtags. This project focuses only on *scrapping* **Photo/Carousel** posts to maintain data consistency.

##  Key Features

* **Accurate Scraping:** Captures Caption, Username, Timestamp, and Post URL.
* **Content Filtering:** Automatically excludes Video/Reels posts.
* **Session Mode:** Supports `cookies.json` to avoid the Login Wall.
* **Output:** Saves results to JSON (and/or CSV) files.

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
