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
python cli.py --tag jokowi --limit 15 
```

```json
[
 {
    "url": "https://www.instagram.com/p/DSWAzXNk69T/",
    "caption": "16 Desember 2025 - Ketum Rampai Nusantara Mardiansyah Semar @semarmardiansyah Kembali Bertemu Dengan Presiden ke-7 RI Joko Widodo @jokowi Sekaligus Dewan Pembina Rampai Nusantara di Kediaman Pribadi Jokowi di Solo, Jawa Tengah 🇮🇩\n\n#jokowi #mardiansyahsemar #semarmardiansyah #rampainusantara #jokowidodo #presidenke7jokowi #dewanpembinarampainusantara #presidenjokowi #gibran #gibranrakabumingraka #gibranrakabuming #ijazahjokowi #tuduhanijazahpalsujokowi\".",
    "username": null,
    "timestamp": "2025-12-17T00:11:15.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/DP8p5mGEvEu/",
    "caption": "Banyak isu yang menyebut IKN sebagai proyek mangkrak, namun wanita ini justru beri kesaksian yang berbeda. Saat berkunjung ke IKN, ia melihat sendiri bagaimana kota ini mempunyai infrastruktur yang rapi, modern, dan tertata dengan perencanaan yang matang. Ia pun membagikan sejumlah foto yang memperlihatkan kondisi sebenarnya di IKN.\n\nFoto: [Tiktok/ra.yuana]\n\n#infonetizone #ikn #nusantara #ibukota #jakarta #indonesia #jokowi #prabowo\".",
    "username": null,
    "timestamp": "2025-10-18T10:46:11.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/CRYyaSSlGa3/",
    "caption": "YNTKS\n\n#viral_padamasanya \n\n#yntkts #ynt #yntktsmeme #yntkns #memeindonesia #memejokowi #jokowi #yanggatau\".",
    "username": null,
    "timestamp": "2021-07-16T12:03:12.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/DSfQ49aEXzV/",
    "caption": "JOKOWI Sang maestro \nFlashback kebelakang\nFahri hamzah dan pks,dulu sekitar tahun 2014 an sampai 2019 an orang yang paling vokal mengkritik habis habisan tentang pak jokowi,tapi sekarang Alhamdulillah luluh lantah,akan kah roy suryo cs sama seperti fahri hamzah yang sekarang\nKita tunggu endingnya\n#jokowi\n#sangorkestra\".",
    "username": null,
    "timestamp": "2025-12-20T14:23:51.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/DSbmzWcE-JE/",
    "caption": null,
    "username": null,
    "timestamp": "2025-12-19T04:18:22.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/DBawIn-S6OM/",
    "caption": "😭😭😭🙏🏻🙏🏻🙏🏻\n•\nsc : tallyfication\n•\ncheck it out 👉🏻 ⌜ @RECEHTAGRAM ⌟ untuk postingan hiburan dan informasi lainnya yang sedang trending ✌🏻\n•\n#recehtagram #memes #indonesia #textpost #funny #mood #explore  #love #happy #2024 #photooftheday #memeoftheday #meme #ngakakkocak #dagelan #lucu #ngakak #lol #instagram #relate #jokowi\".",
    "username": null,
    "timestamp": "2024-10-22T07:26:58.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/DSmBmYmFHTt/",
    "caption": null,
    "username": null,
    "timestamp": "2025-12-23T05:24:56.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/DKgQsNCyXkZ/",
    "caption": "Sindrom Stevens Johnson (SJS) mendadak menjadi perbincangan publik setelah mencuat dugaan bahwa Joko Widodo (Jokowi) mengidap penyakit autoimun langka ini. Dugaan tersebut muncul usai publik mencermati perubahan signifikan pada kondisi kulit wajah dan leher Jokowi dalam beberapa penampilan terakhirnya. \n\nSebelumnya, Ajudan pribadi Jokowi, Kompol Muhammad Fitriansyah mengatakan bahwa mantan presiden tersebut tidak dapat hadir pada upacara Hari Lahir Pancasila 2 Juni 2025 karena tengah mengidap penyakit kulit. “Beliau masih proses penyembuhan dari alergi kulit,” kata Muhammad Fitriansyah.\n\n \nMeski belum ada konfirmasi resmi, kemunculan bercak gelap dan iritasi kulit memunculkan spekulasi bahwa gejala tersebut berkaitan dengan SJS, suatu reaksi hipersensitivitas serius terhadap obat atau infeksi yang menyerang kulit dan selaput lendir. Penyakit ini tergolong langka namun berpotensi fatal jika tidak ditangani dengan cepat. \n\nhttps://lifestyle.sindonews.com/read/1576141/155/mengenal-sindrom-stevens-johnson-penyakit-langka-serius-yang-diduga-diidap-jokowi-1749082000\n\n#Sindonews #SindromStevensJohnson #Jokowi #SJS #JokoWidodo\".",
    "username": null,
    "timestamp": "2025-06-05T03:30:12.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/BqW_IJJAfMY/",
    "caption": "Cuma Presiden Jokowi yang sedekat ini dengan rakyatnya.\n\n@Regran_ed from @jokowi_membangun - - Mengharukan 😭😭😭\n.\n.\n.\n.\n.\n#dukungjokowi #jokowi #jkw4p #2019pilihjokowi #2019jokowiaja #sahabatjokowi #jokowi2periode #2periode #jokowipresidenku #t3tapjokowi #2019t3tapjokowi #eramilenial #2019jokowilagi #memejokowi #jokowi #jokowimarufamin #2019pilihjokowi #irianajokowi  #jokowipresidenkitasemua #diasibukkerja #prestasijokowi #kinerjajokowi #pilpres2019 #merakyat #jokowipresidenku #pemimpin #jokowiforpresident #2019jokowiaja #2019tetapjokowi\".",
    "username": null,
    "timestamp": "2018-11-19T10:50:26.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/DRzLOqmEixB/",
    "caption": "Tiga Pilar Republik \n\nSource : Tiktok @owi.bradpit\n\nIzinnn🙏\n\nFollow akun ini segera!!! Kenapa? Ya gpp follow aja. \n\n#memes #meme #memedaily #memeindo #memeid #memepage #memeasw #republicofmeme #memerelate #jokowi #prabowo #anisbaswedan #anakabah #culture #skena #outfit #ootd #4u #beranda #fyp\".",
    "username": null,
    "timestamp": "2025-12-03T11:27:48.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/CqVKxkOPFOo/",
    "caption": "Aku menyebutnya tampan dan pemberani\n\nSource : FB\n\n#meme #jokowi #memeindonesia #kegoblokanunfaedah #kelakuanwarga62 #rabucringe #memecringe #asupanmeme #antijedagjedug #memeabsurd #hatihatidiinternet\".",
    "username": null,
    "timestamp": "2023-03-28T11:22:14.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/DPd5anfkhJ9/",
    "caption": null,
    "username": null,
    "timestamp": "2025-10-06T12:05:18.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/DSfCUY5kzoX/",
    "caption": null,
    "username": null,
    "timestamp": "2025-12-20T12:16:32.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/DMjtOnAqW3y/",
    "caption": "Jokowi dan Iriana tinggalkan kediaman di Solo pagi ini. Saat ditanya tujuannya, ia hanya menjawab singkat: \"Ke Jogja.\" \n-\n- \n#Jokowi #Solo #Yogyakarta #mdkan\".",
    "username": null,
    "timestamp": "2025-07-26T04:40:42.000Z",
    "source_tag": "jokowi"
  },
  {
    "url": "https://www.instagram.com/p/DKeRtfSJXkS/",
    "caption": "Misteri sakit Pak Jokowi? 🤔💭\n\n#Pancasila #JokoWidodo #Jokowi #HarlahPancasila #HariLahirPancasila #alergikulit #pinterpolitik #infografis #politikindonesia #beritapolitik #beritapolitikterkini\".",
    "username": null,
    "timestamp": "2025-06-04T09:00:34.000Z",
    "source_tag": "jokowi"
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
