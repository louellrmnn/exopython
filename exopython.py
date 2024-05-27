import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to convert star rating to numerical value
def convert_rating(rating_str):
    ratings = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    for key in ratings:
        if key in rating_str:
            return ratings[key]
    return 0

# Function to scrape a single page
def scrape_page(page_num):
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    books = []
    for article in soup.select('article.product_pod'):
        book = {}
        book['title'] = article.find('h3').find('a')['title']
        book['star-rating'] = convert_rating(article.find('p', class_='star-rating')['class'][1])
        book['price'] = float(article.find('p', class_='price_color').get_text(strip=True)[1:])
        books.append(book)
    
    return books

# Scrape the first 10 pages
all_books = []
for page_num in range(1, 11):
    all_books.extend(scrape_page(page_num))

# Create a DataFrame to display the books
df_books = pd.DataFrame(all_books, columns=['title', 'star-rating', 'price'])

# Filter books with 3 stars or more and price above 20.00
filtered_books = df_books[(df_books['star-rating'] >= 3) & (df_books['price'] > 20.00)]

# Write the results to a CSV file
filtered_books.to_csv('result.csv', index=False, encoding='utf-8')

print("Le fichier result.csv a été créé avec succès.")
