# Books_Scraper 📚

Multi-page books scraper using XPath, Python, lxml, and CSV export — Day 2 project  

## 📝 Project Overview  
This project scrapes book data (title, price, rating) from the sample website [books.toscrape.com](http://books.toscrape.com/) using XPath with Python. It navigates multiple pages, extracts data from every book, and exports the results to a CSV file.  

**Why this project matters:**  
- Demonstrates core web‑scraping skills: HTTP requests, HTML parsing, XPath selection, pagination  
- Exports structured data for further analysis (CSV), making it useful for price/rating analysis, data exploration or portfolio showcase  
- Easy to extend: you or others can adapt it to different websites by changing XPaths or URL patterns  

---

## ✅ Features  
- Fetches multiple pages (configurable) automatically  
- Parses each book item’s title, price, and rating  
- Uses XPath (via `lxml`) for robust and precise element selection  
- Stores all scraped data in `books.csv` (UTF‑8 encoded, Excel‑ready)  
- Simple, clean Python script — easy to read and understand  

---

## 🧰 Requirements  
- Python 3.x  
- Libraries: `requests`, `lxml`, `pandas`  
  ```bash
  pip install requests lxml pandas
