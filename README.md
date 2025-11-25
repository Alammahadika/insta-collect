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

**Scraping 15 Photo posts with Cookies:**
```bash
python cli.py --tag jokowi --limit 5 --cookie cookies.json
```
## Hasil Scraping — Hashtag #jokowi

 mymac@mymacs-MacBook-Air insta-collect % python cli.py --tag jokowi --limit 5
[*] Target: #jokowi | Limit: 5

{
    "url": "https://www.instagram.com/p/DLOvv7tP4ra/",
    "caption": "@jokowi baru-baru ini diduga mengalami alergi kulit setelah kunjungan ke Vatikan, menyebabkan perubahan fisik di wajah beliau. \n\nNamun, ajudan presiden ke-7 RI memastikan bahwa kondisi fisiknya tetap stabil dan tidak mengganggu aktivitasnya, Minggu (22/6/2025). 💪\n\n\"Secara visual (kulit), kita bisa lihat Bapak memang agak berubah. Secara fisik oke, tidak ada masalah\" kata Kompol Syarif Muhammad Fitriansyah.\n\nDoakan semoga proses pemulihannya semakin cepat ya untuk Pak Jokowi! 🙏\n\nBaca selengkapnya di: xyzonemedia.com\n\nShare the news and vibe with @xyzonemedia to be featured! ✨\n\n📸: Detik.com\n\n#XYZONEmedia #XYZONE #XYZmedia #XYZcreativemedia #Jokowi #Alergi #Jokowidodo #News\".",
    "username": null,
    "timestamp": "2025-06-23T04:46:39.000Z",
    "source_tag": "jokowi"
  },
  


{
    "url": "https://www.instagram.com/p/DRdp_HDkjxI/",
    "caption": null,
    "username": null,
    "timestamp": null,
    "source_tag": "jokowi"
  },
 
 


{
    "url": "https://www.instagram.com/p/DRb8qWjjCBf/",
    "caption": "@jokowi baru-baru ini diduga mengalami alergi kulit setelah kunjungan ke Vatikan, menyebabkan perubahan fisik di wajah beliau. \n\nNamun, ajudan presiden ke-7 RI memastikan bahwa kondisi fisiknya tetap stabil dan tidak mengganggu aktivitasnya, Minggu (22/6/2025). 💪\n\n\"Secara visual (kulit), kita bisa lihat Bapak memang agak berubah. Secara fisik oke, tidak ada masalah\" kata Kompol Syarif Muhammad Fitriansyah.\n\nDoakan semoga proses pemulihannya semakin cepat ya untuk Pak Jokowi! 🙏\n\nBaca selengkapnya di: xyzonemedia.com\n\nShare the news and vibe with @xyzonemedia to be featured! ✨\n\n📸: Detik.com\n\n#XYZONEmedia #XYZONE #XYZmedia #XYZcreativemedia #Jokowi #Alergi #Jokowidodo #News\".",
    "username": null,
    "timestamp": null,
    "source_tag": "jokowi"
  },
 
 


{
    "url": "https://www.instagram.com/p/DFMPnM5SJ0r/",
    "caption": "@jokowi baru-baru ini diduga mengalami alergi kulit setelah kunjungan ke Vatikan, menyebabkan perubahan fisik di wajah beliau. \n\nNamun, ajudan presiden ke-7 RI memastikan bahwa kondisi fisiknya tetap stabil dan tidak mengganggu aktivitasnya, Minggu (22/6/2025). 💪\n\n\"Secara visual (kulit), kita bisa lihat Bapak memang agak berubah. Secara fisik oke, tidak ada masalah\" kata Kompol Syarif Muhammad Fitriansyah.\n\nDoakan semoga proses pemulihannya semakin cepat ya untuk Pak Jokowi! 🙏\n\nBaca selengkapnya di: xyzonemedia.com\n\nShare the news and vibe with @xyzonemedia to be featured! ✨\n\n📸: Detik.com\n\n#XYZONEmedia #XYZONE #XYZmedia #XYZcreativemedia #Jokowi #Alergi #Jokowidodo #News\".",
    "username": null,
    "timestamp": null,
    "source_tag": "jokowi"
  },
 



 

{
    "url": "https://www.instagram.com/p/DRdrw5HkkJB/",
    "caption": "Tapanuli Selatan di Bawah Langit yang Menangis: Jalan Amblas, Sungai Mengganas\n\nTapanuli Selatan di bawah langit yang menangis—itulah yang terlihat beberapa hari terakhir. Awan hitam menggulung tanpa henti, hujan deras jatuh seperti ingin menguji ketahanan bumi dan manusia yang tinggal di bawahnya. Dan akhirnya, bumi itu menyerah. Pada malam 24 November 2025, di Kelurahan Rianiate, Kecamatan Angkola Sangkunur, jalan nasional yang menghubungkan Tapanuli Selatan dan Mandailing Natal amblas sedalam belasan meter, tepat di dekat Danau Siais. Akses transportasi? Terhenti total.\n\nSebelum cerita itu makin berat, seruput dulu kopi Sipirok—pahitnya menenangkan, hangatnya memberi kekuatan. Tapi di tepi Danau Siais, tanah yang selama ini setia memeluk jalan mendadak retak. Retakan kecil berubah menjadi jurang besar. Jalan yang sehari-hari menjadi urat nadi ekonomi, jalur sekolah, tempat ribuan cerita berlalulalang kini lenyap begitu saja. Asap kendaraan dan klakson yang biasanya riuh, digantikan keheningan yang mencekam.\n\nPagi harinya, Sungai Sangkunur meluap, banjir besar menerjang Desa Simataniari, sekitar 160 kepala keluarga terdampak, ketinggian air mencapai satu meter. Di Rianiate, 86 rumah di Lingkungan I ikut terendam oleh luapan Sungai Batang Toru. Warga berdiri di halaman rumah yang mulai tergenang, menatap ke bawah dengan dada berdebar. Jalan itu lebih dari sekadar jalan—itu adalah harapan. Dan kini, harapan itu terputus.\n\nMeski alam marah, manusia Tapanuli Selatan tetap teguh. Warga saling membantu, menyalakan lampu kecil, memindahkan anak-anak, berbagi makanan, dan menjaga satu sama lain. Badai boleh datang, jalan boleh runtuh, rumah boleh terendam, tapi keteguhan mereka tak terkalahkan. Dan ketika pagi cerah akhirnya tiba, mereka tahu—dari puing dan air mata, kehidupan akan dibangun kembali.\n\nBPBD Tapanuli Selatan kini turun tangan, memantau, mendata, dan menyiapkan langkah darurat. Di tengah hujan yang belum reda, harapan tetap menyala.\n\n📸 Foto hanya AI \n#prabowo subianto \n#jokowi\n#kopisipirok \n#Bencana Alam\n#Tapsel\".",
    "username": null,
    "timestamp": "2025-11-25T03:08:48.000Z",
    "source_tag": "jokowi"
  }
]
