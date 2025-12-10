import requests
from lxml import etree
import pandas as pd
import time

# ======================
# CONFIG
# ======================
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
MAX_PAGES = 5   # Number of pages to scrape
DELAY = 1       # Delay between requests in seconds
all_books = []  # List to store all scraped books

# Mapping rating words to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# ======================
# SCRAPING LOOP
# ======================
for page in range(1, MAX_PAGES + 1):
    url = BASE_URL.format(page)
    print(f"Scraping page {page}: {url}")
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page {page}")
        continue
    
    tree = etree.HTML(response.text)
    
    # Select all book nodes
    books = tree.xpath("//article[contains(@class,'product_pod')]")
    
    for book in books:
        # Extract title
        title = book.xpath(".//h3/a/@title")[0]
        
        # Extract price
        price = book.xpath(".//p[@class='price_color']/text()")[0]
        
        # Extract rating
        rating_class = book.xpath(".//p[contains(@class,'star-rating')]/@class")[0]
        rating_word = rating_class.split()[1]  # e.g., 'Three'
        rating = rating_map.get(rating_word, 0)
        
        # Append to all_books list
        all_books.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })
    
    time.sleep(DELAY)  # polite scraping

# ======================
# EXPORT TO CSV
# ======================
df = pd.DataFrame(all_books)
df.to_csv("books.csv", index=False, encoding="utf-8-sig")
print(f"Scraping completed! {len(all_books)} books saved to books.csv")
