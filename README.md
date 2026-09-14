# Books Web Scraping & Data Cleaning

## Project Overview

This project is a Python-based web scraping and data cleaning project using the **Books to Scrape** website.

The project collects book information from **50 pages** of the website and stores the scraped data in an Excel dataset. The collected data is then cleaned and prepared for further analysis.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- OpenPyXL
- Microsoft Excel

## Data Collected

The scraper collects the following information:

- Book Name
- Price
- Rating
- Availability
- Category
- Product URL

## Project Workflow

```text
Books to Scrape Website
        ↓
Requests
        ↓
BeautifulSoup
        ↓
50 Pages
        ↓
1,000 Records
        ↓
Book Details
        ↓
Product URLs & Category
        ↓
Data Cleaning
        ↓
Excel Dataset
```

## Web Scraping

The project uses **Requests** to send HTTP requests and **BeautifulSoup** to parse the HTML content of the website.

The scraper processes 50 pages and extracts book details including name, price, rating, availability, category, and product URL.

## Data Cleaning

The `clean_data.py` script performs several data cleaning operations:

- Removes currency symbols from the Price column
- Converts Price values into numeric format
- Converts rating words into numbers
- Cleans Availability values
- Handles missing values
- Removes duplicate records
- Resets the DataFrame index
- Saves the cleaned data to an Excel file

## Project Files

| File | Description |
| `scraper.py` | Basic web scraping script |
| `scraper_final.py` | Detailed web scraping script |
| `clean_data.py` | Data cleaning script |
| `final_books_data.xlsx` | Scraped book dataset |
| `workflow.txt` | Project workflow |
```
## Output

The project generates an Excel dataset containing the scraped book information.

## Key Learning Outcomes

Through this project, I gained practical experience in:

- Web scraping with Python
- HTML parsing using BeautifulSoup
- Sending HTTP requests
- Working with Pandas DataFrames
- Data cleaning and preprocessing
- Handling missing and duplicate data
- Exporting data to Excel
- Working with product URLs and structured datasets

## Source Website

The project uses **Books to Scrape**, a website designed for practicing web scraping.