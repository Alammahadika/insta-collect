# insta-collect: Modular Instagram Data Collector

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
| `--tag` | The hashtag to scrape (without `#`). | Yes | `gibran` |
| `--limit` | Number of PHOTO posts to scrape. | No (Default: 10) | `10` |
| `--cookie` | Path to `cookies.json`. **Highly recommended.** | No | `cookies.json` |

### Example Usage

**Scraping Photo posts with Cookies:**
```bash
python cli.py --tag gibran --limit 10 --cookie cookies.json
```

```json
[
  {
    "url": "https://www.instagram.com/p/DPQa9CnAAMN/",
    "caption": "Selamat Ulang Tahun mas Gibran @gibran_rakabuming Wakil Presiden Republik Indonesia 🇲🇨🇲🇨🇲🇨. \n\nDoa terbaik buat mas Gibran, sehat2, bahagia dan sukses selalu 🙏🙏🙏\n\n#gibran #gibranrakabumingraka #wapres #wakilpresiden\".",
    "username": null,
    "timestamp": "2025-10-01T06:29:00.000Z",
    "source_tag": "gibran"
  },
  {
    "url": "https://www.instagram.com/p/DRW6FsZkqgl/",
    "caption": null,
    "username": null,
    "timestamp": "2025-11-22T11:59:18.000Z",
    "source_tag": "gibran"
  },
  {
    "url": "https://www.instagram.com/p/DKetH71yBnZ/",
    "caption": "Forum Purnawirawan TNI mengajukan surat usulan pemakzulan Gibran Rakabuming Raka ke DPR pada 2 Juni 2025. Mereka menilai pencalonan Gibran sebagai wakil presiden memunculkan potensi konflik kepentingan, merujuk pada keterlibatan Anwar Usman dalam putusan MK No. 90/PUU-XXI/2023.\n\nDalam surat tersebut, mereka mendorong MPR memproses pemakzulan sesuai ketentuan Pasal 7A dan 7B UUD 1945. Selain aspek hukum, disoroti pula isu kepatutan dan moralitas, termasuk latar belakang pendidikan, pengalaman, serta dugaan keterlibatan dalam akun media sosial dan laporan KKN yang sedang ditangani KPK.\n\nSementara itu, mantan Presiden Jokowi, Ketua MPR Ahmad Muzani, dan Sekjen Partai Golkar Sarmuji menegaskan bahwa Gibran adalah wakil presiden sah berdasarkan hasil Pemilu 2024. Pemakzulan sendiri baru dapat dimulai jika disetujui oleh dua pertiga anggota DPR dalam rapat paripurna, yang menjadi tantangan tersendiri secara politis.\n\nBaca selengkapnya di kuncihukum.com\n\n#KunciHukum #JawabanAkurat #InformasiTepat #Pemakzulan #Gibran #DPR\".",
    "username": null,
    "timestamp": "2025-06-04T13:01:37.000Z",
    "source_tag": "gibran"
  },
  {
    "url": "https://www.instagram.com/p/DRd2ZCgkcjB/",
    "caption": null,
    "username": null,
    "timestamp": "2025-11-25T05:21:35.000Z",
    "source_tag": "gibran"
  },
  {
    "url": "https://www.instagram.com/p/DL304L9Cns9/",
    "caption": "💯 Chasing constant comfort can slowly dull the fire within us that craves growth, adventure, and meaning. \n\nWhen we prioritize ease and safety above all else, we stop taking risks, stop dreaming boldly, and settle for a life that feels secure but empty. \n\nThe soul thrives on challenge and purpose, and too much comfort can suffocate that inner spark that makes us feel truly alive. \n\nComment your thoughts 💭...\n\nFollow @WiseSages for daily wisdom 🦉\n\n.\n.\n#khalilgibran #gibran #comfort #quotesandsayings #realtalk\".",
    "username": null,
    "timestamp": "2025-07-09T03:40:21.000Z",
    "source_tag": "gibran"
  },
  {
    "url": "https://www.instagram.com/p/DRUHz7ckXot/",
    "caption": null,
    "username": null,
    "timestamp": "2025-11-21T10:01:29.000Z",
    "source_tag": "gibran"
  },
  {
    "url": "https://www.instagram.com/p/DJ6FfXryw-i/",
    "caption": "(Berita selengkapnya cek IG Stories @kompascom)\n\nPolitikus Partai Solidaritas Indonesia (PSI), Ade Armando, menilai bahwa Gibran Rakabuming Raka adalah wakil presiden (wapres) terbaik sepanjang sejarah Indonesia. \n\nAde menilai kehadiran Gibran sebagai wapres tidak seharusnya dilihat dari statusnya sebagai putra mantan Presiden Joko Widodo (Jokowi). \n\nIa meyakini Gibran adalah pendorong elektabilitas Prabowo pada Pemilu 2024.\n\n“Nah, begitu juga saya ingin orang melihat, eh naiknya Gibran itu, diangkatnya Gibran sebagai wapres, jangan dilihat karena dia anak Jokowi sebagai dinasti. Gibran itu adalah faktor yang menaikkan suaranya Pak Prabowo,” ujar Ade dalam Podcast Gaspol Kompas.com, dikutip Rabu (21/5/2025). \n\nAde menyebut, Gibran telah menunjukkan sejumlah pencapaian yang signifikan. Dia pun memuji gaya komunikasi Gibran yang memanfaatkan media sosial untuk menyampaikan pesan kepada publik.\n\nPenulis: Tria Sutrisna\nEditor: Jessi Carina\n\n + #AdeArmando #Gibran #GibranRakabuming #Wapres #Gaspol\".",
    "username": null,
    "timestamp": "2025-05-21T07:41:11.000Z",
    "source_tag": "gibran"
  },
  {
    "url": "https://www.instagram.com/p/DRa7Q1kk7ak/",
    "caption": null,
    "username": null,
    "timestamp": "2025-11-24T01:26:31.000Z",
    "source_tag": "gibran"
  },
  {
    "url": "https://www.instagram.com/p/CxWMwPsLuf6/",
    "caption": "“If your heart is a volcano, how shall you expect flowers to bloom?”\n\n#khalilgibran #theprophet #gibran #poetry #quotes #love\".",
    "username": null,
    "timestamp": "2023-09-18T20:38:33.000Z",
    "source_tag": "gibran"
  },
  {
    "url": "https://www.instagram.com/p/DRdLXLNE3QZ/",
    "caption": "🚨 INDONESIA MASUK MODE NEXT LEVEL!\n\nWapres Gibran ngomongin $Bitcoin & crypto di acara G20 Summit, dan ini bukan hal kecil. Indonesia nunjukin kalau kita nggak mau cuma jadi penonton kita mulai ikutan dalam pembahasan aset digital bareng negara-negara ekonomi terbesar dunia.\n\nLangkah ini jadi sinyal kuat kalau arah kebijakan Indonesia makin terbuka sama inovasi finansial dan potensi ekonomi baru dari crypto. Buat pelaku market lokal, ini semacam “lampu hijau” kalau game baru udah dimulai, dan Indonesia nggak mau ketinggalan.\n\nSimpelnya: ini bullish untuk adopsi. Dan kita akhirnya punya suara di meja besar.\n\n#indonesianews #bitcoin #gibran #cryptonews\".",
    "username": null,
    "timestamp": "2025-11-24T22:25:41.000Z",
    "source_tag": "gibran"
  }
]


```



***

## Behind the Scenes: How the Scraper Works

When executed, the script uses the Playwright browser to automate the following steps:

1.  **Session Resumption:** Loads `cookies.json` to automatically resume your logged-in Instagram session.
2.  **Hashtag Scan:** Navigates to the hashtag page and automatically scrolls to collect post links up to the specified limit.
3.  **Data Extraction:** Visits each individual post URL and uses multiple strategies (Meta Tags and selectors) to scrape the Caption, Username, and Timestamp.
4.  **Filtering:** Filters the final dataset to only include photo/carousel posts, removing all video content.

***
