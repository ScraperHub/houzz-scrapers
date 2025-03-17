# houzz-scrapers

## Description

This repository contains Python-based scrapers for extracting product data from Houzz. The scrapers utilize requests for making HTTP requests and BeautifulSoup for parsing HTML content. The extracted data includes product listings and detailed product information, making it valuable for market analysis, competitor research, and e-commerce insights.

➡ Read the full blog [here](https://crawlbase.com/blog/how-to-scrape-houzz-data/) to learn more.

## Scraper Overview

### Houzz Product Listings Scraper

The `houzz_listings_scraper.py` extracts product details from search results, including:

- **Title**
- **Price**
- **Rating**
- **Image URL**
- **Product Page Link**

This scraper automatically paginates through multiple pages to ensure a comprehensive extraction of product listings.

### Houzz Product Page Scraper

The `houzz_product_scraper.py` extracts detailed product information from individual product pages, including:

- **Title**
- **Price**
- **Description**
- **Image URLs**
- **Product Page Link**

This scraper provides in-depth product insights by gathering additional details available only on individual product pages.

## Environment Setup

Ensure Python is installed on your system. Check the version using:

```bash
python --version
```

Install the required dependencies:

```bash
pip install requests beautifulsoup4
```

- **requests** – Handles HTTP requests.
- **BeautifulSoup** – Parses HTML to extract structured data.

## Running the Scrapers

### 1. Run the Product Listings Scraper

Extract product listings and save the data as JSON:

```bash
python houzz_listings_scraper.py
```

### 2. Run the Product Page Scraper

Use product page URLs from the listings to extract detailed information:

```bash
python houzz_product_scraper.py
```

The extracted data will be saved in JSON files.

## To-Do List

- Extract additional details like customer reviews and specifications.
- Add support for exporting data to CSV.
- Implement better error handling and retries.
- Optimize pagination handling for large-scale scraping.
