# web_scrap_price
 This Python script scrapes live cryptocurrency prices from Arzdigital and gold prices from Iranjib. It collects the asset names and prices, then stores them in a CSV file for easy access and analysis. The project utilizes BeautifulSoup and requests for web scraping, and the data is saved with the current date.

## Features
- Scrapes cryptocurrency prices from Arzdigital.
- Scrapes gold prices from Iranjib.
- Saves the collected data into a CSV file, with columns for date, asset name, price, and source.

## Technologies Used
- `BeautifulSoup` for parsing HTML content.
- `requests` for fetching webpage data.
- `csv` module for saving data in CSV format.
- `datetime` for capturing the current date.

## How to Use
1. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
