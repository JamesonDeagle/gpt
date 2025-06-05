# Threads Scraper

This repository contains a simple Python script for collecting posts from a public user on [Threads](https://www.threads.net/). The script uses the `threads-api` package and does not require authentication for scraping public accounts.

## Requirements

- Python 3.11
- `threads-api` and its dependencies

The required libraries can be installed with `pip`:

```bash
pip install threads-api cryptography colorama instagrapi==1.19.8 Pillow
```

## Usage

Run the scraper with a Threads username. Optionally provide an output filename (defaults to `<username>_threads.json`).

```bash
python threads_scraper.py <username> [output_file]
```

Example:

```bash
python threads_scraper.py zuck zuck_posts.json
```

The script writes the retrieved threads data as JSON.
