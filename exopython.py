import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape a single page
def scrape_page(page_num):
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')