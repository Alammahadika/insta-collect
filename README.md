# instacollect: Modular Instagram Data Collector

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
* **CSV & XLXS Output:** Adding an option to save data in CSV and XLSX format.

***
## Naming Conventions: _ vs - in Python Projects
| Context | Use | Example |
|------|------|------|
| Package name (PyPI / GitHub) | `-` (hyphen) | insta-collect |
| Python package directory | `_` (underscore) | insta_collect |
| Python import statement | `_` (underscore) | import insta_collect |
| CLI execution via module | `_` (underscore) | python -m insta_collect.cli |
| Script / file name | flexible | insta-collect.py |

## Setup and Installation

Install **insta-collect** using `pip`:
```bash
pip install insta-collect
```
### or
```bash
pip install git+https://github.com/Alammahadika/insta-collect.git
```

### Playwright Setup (Required)

`insta-collect` relies on **Playwright** for browser automation.  
After installation, install the required browser binaries once:

```bash
playwright install
```

### Prepare Cookies (Highly Recommended)

To avoid being blocked or receiving `null` data when scraping many posts, it is strongly recommended to use a logged-in Instagram session.

Steps:

- Export your Instagram session cookies from your browser
- Save the file as `cookies.json`
- Place it in your working directory

**Important:**  
Add `cookies.json` to `.gitignore` to prevent leaking credentials.

---

## How to Run the Scraper

Once installed, the scraper is available as a **CLI command**.

### Available Arguments

| Argument | Description | Required | Example |
|--------|------------|----------|---------|
| `--tag` | Hashtag to scrape (without `#`) | Yes | `prabowo` |
| `--limit` | Number of PHOTO posts to scrape | No (default: 15) | `15` |
| `--cookie` | Path to `cookies.json` | No (recommended) | `cookies.json` |

### Example Usage
```bash
cd /Users/mymac/Desktop/insta-collect
```
```bash
insta-collect --tag prabowo --limit 15
```


```json
[
 {
    "url": "https://www.instagram.com/p/DSSGF1bEzoR/",
    "caption": "Presiden Prabowo Subianto menyinggung pihak-pihak yang teriak agar ditetapkan status darurat bencana nasional. Prabowo memastikan pemerintah bisa mengatasi dampak bencana di Aceh, Sumatera Utara, dan Sumatera Barat. \n \nHal itu disampaikan Prabowo dalam Sidang Kabinet Paripurna, di Istana Negara, Jakarta, Senin (15/12/2025). Prabowo menyebut semua kekuatan sudah dikerahkan ke lokasi bencana dan situasi kini terkendali. \n   \n         \n📰: Detik.com  \nhttps://news.detik.com/berita/d-8260962/prabowo-ada-yang-teriak-teriak-soal-bencana-nasional-ini-3-dari-38-provinsi \n📹:    \n          \nIkuti Perkembangan Politik Terkini di Total Politik!                                    \n.............................                                    \n#TotalPolitik #Prabowo #aceh #sumatera\".",
    "caption_status": "long_text",
    "timestamp": "2025-12-15T11:39:23.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DSZbafLFfaX/",
    "caption": "Greenpeace Indonesia dan Yayasan Pusaka Bentala Rakyat menyebut keinginan Presiden Prabowo Subianto menanam kelapa sawit, tebu, dan singkong di Papua bisa membawa bencana ekologis ke Papua.\n\n“Demi ambisi swasembada pangan dan energi, Prabowo menyiapkan bencana ekologis bagi Papua,” kata Juru Kampanye Hutan Greenpeace Indonesia, Asep Komarudin, dalam pernyataan tertulis yang diterima Tempo, 17 Desember 2025.\n\nBaca selengkapnya di tempo.co dan link in bio.\n\n#tempodotco #Greenpeace #Prabowo\".",
    "caption_status": "short_text",
    "timestamp": "2025-12-18T08:00:22.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DPzfPS2k6io/",
    "caption": null,
    "caption_status": "no_text",
    "timestamp": "2025-10-14T21:19:52.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DSly7Buged1/",
    "caption": null,
    "caption_status": "no_text",
    "timestamp": "2025-12-23T03:16:41.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DSuFswdE7mq/",
    "caption": null,
    "caption_status": "no_text",
    "timestamp": "2025-12-26T08:34:40.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DPcp6FxEmcY/",
    "caption": "Sudah setahun berlalu sejak Prabowo resmi menjabat Presiden Indonesia. Bagaimana realisasi janji kampanyenya? 🤔\n\nTulis pendapatmu di kolom komentar dibawah!\n👉 Follow @getconnectx | Artikel lengkap di getconnectx.com | Forum gratis di getconnectx.com/forum\n\n#RaporPrabowo #PresidenIndonesia #Prabowo #Kampanye #Realisasi\".",
    "caption_status": "short_text",
    "timestamp": "2025-10-06T00:30:05.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DSe2u_vkxQX/",
    "caption": "Presiden Prabowo Subianto menyinggung pencapaian kontingen Indonesia di SEA Games 2025 Thailand yang telah memperoleh 91 medasi emas hingga Jumat (19/12/2025) malam. \n \nHal ini ia sampaikan saat memberikan sambutan dalam kegiatan Gelaran Akad Serentak Rumah Subsidi se-Indonesia di Serang, Banten, Sabtu (20/12/2025). \n \nPrabowo mula-mula menyampaikan apresiasi kepada Menteri Pemuda dan Olahraga (Menpora) Erick Thohir yang turut hadir dalam acara tersebut atas prestasi kontingen Indonesia dalam SEA Games 2025 Thailand. \n  \nPrabowo mengaku bangga dengan pencapaian tersebut. Akan tetapi, sambil bercanda, ia mengaku merasa pusing dengan bonus yang akan diberikan kepada para peraih medali emas. \n       \n📰: Tirto.id \n                                      \nIkuti Perkembangan Politik Terkini di Total Politik!               \n.............................                \n#TotalPolitik #Prabowo #SeaGamesThailand #Sumatra #aceh\".",
    "caption_status": "long_text",
    "timestamp": "2025-12-20T10:35:19.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DP8p5mGEvEu/",
    "caption": "Banyak isu yang menyebut IKN sebagai proyek mangkrak, namun wanita ini justru beri kesaksian yang berbeda. Saat berkunjung ke IKN, ia melihat sendiri bagaimana kota ini mempunyai infrastruktur yang rapi, modern, dan tertata dengan perencanaan yang matang. Ia pun membagikan sejumlah foto yang memperlihatkan kondisi sebenarnya di IKN.\n\nFoto: [Tiktok/ra.yuana]\n\n#infonetizone #ikn #nusantara #ibukota #jakarta #indonesia #jokowi #prabowo\".",
    "caption_status": "short_text",
    "timestamp": "2025-10-18T10:46:11.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DSwB9T8kacM/",
    "caption": "NEGARA MERUGI ULAH ASING?! 😱💥\n\nPresiden Prabowo angkat suara soal kebocoran anggaran negara. 💸\nIa bahkan menyinggung adanya kekuatan asing yang diduga ikut bermain! 😳\n\nPenyelamatan Rp6 triliun disebutnya baru sebagian kecil dari kerugian besar yang selama ini terjadi.⚠️\n\nKini, perang melawan korupsi ditegaskan akan dilakukan tanpa pandang bulu!🚨\n\nHukum diminta tegas, lobi ditolak, dan kekayaan negara harus diselamatkan.🇮🇩\n\nApakah ini awal perubahan besar? Atau justru akan banyak pihak yang “kepanasan”? 👀🔥\n\n#Prabowo #Korupsi #BeritaPolitik #Bitorex #Bitorex_Ltd\".",
    "caption_status": "long_text",
    "timestamp": "2025-12-27T02:40:28.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DSmySpzElXP/",
    "caption": null,
    "caption_status": "no_text",
    "timestamp": "2025-12-23T12:30:13.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DP40j6nEy6p/",
    "caption": "Presiden Prabowo baru saja meneken Perpres baru soal waste to energy & Indonesia akhirnya mulai serius ubah sampah jadi sumber energi. \n\nProyek ini bakal dimulai di 10 kota, termasuk Bantar Gebang dan Langkah besar kalau berhasil, ini bisa jadi titik balik pengelolaan sampah nasional.\n\nApakah kita siap melihat gunung sampah berubah jadi sumber energi masa depan?\n\n#WasteToEnergy #EnergiHijau #SahamIndonesia #Danantara #PLN #prabowo\".",
    "caption_status": "short_text",
    "timestamp": "2025-10-16T23:02:24.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DSpPs8bkZxO/",
    "caption": null,
    "caption_status": "no_text",
    "timestamp": "2025-12-24T11:25:52.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DPgsmF7j-hs/",
    "caption": null,
    "caption_status": "no_text",
    "timestamp": "2025-10-07T14:11:00.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DRzLOqmEixB/",
    "caption": "Tiga Pilar Republik \n\nSource : Tiktok @owi.bradpit\n\nIzinnn🙏\n\nFollow akun ini segera!!! Kenapa? Ya gpp follow aja. \n\n#memes #meme #memedaily #memeindo #memeid #memepage #memeasw #republicofmeme #memerelate #jokowi #prabowo #anisbaswedan #anakabah #culture #skena #outfit #ootd #4u #beranda #fyp\".",
    "caption_status": "short_text",
    "timestamp": "2025-12-03T11:27:48.000Z",
    "source_tag": "prabowo"
  },
  {
    "url": "https://www.instagram.com/p/DSWwAQEAKnO/",
    "caption": "Prabowo: Papua tanam sawit untuk BBM swasembada energi! Hemat triliun APBN, target 5 tahun. #SwasembadaEnergi #Prabowo #mdkan #mdknbl\".",
    "caption_status": "short_text",
    "timestamp": "2025-12-17T07:02:37.000Z",
    "source_tag": "prabowo"
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


## How to Collect Comments from HTML

In addition to live scraping via Playwright, **Insta-Collect** also supports parsing Instagram comments directly from a previously saved HTML file.

This feature is useful when:
- Download the Instagram HTML file you want to analyze (e.g., kimjongun.html).
- Place it in a folder where you have read/write access (e.g., Desktop, Downloads, or a dedicated project folder).
- Run the CLI from the folder containing your HTML file:

### Supported Outputs
- **JSON** (default)
- **XLSX (Excel)**  
Both files are saved automatically without additional flags.

---

### Example Usage

```bash
cd ~/path/to/your/html
```

```bash
insta_collect % python3 insta-collect.py kimjongun.html --preview 34
```

### Terminal Output

```text
[+] Total entries saved: 119
[+] JSON output: instagram_comments.json
[+] XLSX output: instagram_comments.xlsx

--- PREVIEW ---
1. @brics_countries: 📰 BREAKING NEWS: North Korea Accuses Israel of War Crimes in Gaza 🇰🇵🇮🇱🇵🇸
2. @brics_countries: 📰 BREAKING NEWS: North Korea Accuses Israel of War Crimes in Gaza 🇰🇵🇮🇱🇵🇸 North Korea has strongly con...
3. @karldavid801: Coming from him is hilarious 😂
4. @minoughm: 🙏🙏🙏🙏🙏🙏❤️❤️❤️❤️
5. @nowakb072: Jeśli to prawda to po raz pierwszy biję im brawo
6. @santucci_3.0: Sorry mas quem é Coreia do Norte para falar em genocídio??
7. @akhmedovarsen47: 🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🤲🤲🤲🤲🤲
8. @dn.9795: So now you adore him? Yesterday all of you thought he is one of the bad leaders ever...
9. @carolina17181922: Jamás pensé en estar de acuerdo con corea del norte en algo 💔
10. @mahdi.14almahdi: Free free palestine 🌱🍉
...
34. @michael.croy: As long as the 🇺🇸 USA continue giving Israel an average of $10m...
```

### Output Files

After execution, the following files are generated automatically:

- `instagram_comments.json`
- `instagram_comments.xlsx`

### Data Fields

Each comment entry contains structured fields such as:

- `username`
- `comment_text`
- `timestamp` (if available)
- `source_file`

### Use Cases

This output is immediately usable for:

- Qualitative discourse analysis  
- Sentiment analysis  
- Network / actor mapping  
- Archival research workflows  

### Notes

- No Bash scripting or manual file handling is required  
- Output filenames are generated automatically  
- Preview mode does not affect saved data  
- This feature is currently **experimental** and may evolve in future releases  

## Ethical Use Notice

This tool is intended strictly for academic research, journalism, and public-interest analysis.
Users are responsible for complying with Instagram’s Terms of Service and applicable laws.

