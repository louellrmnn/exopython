import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape a single page
def scrape_page(page_num):
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    books = []
    for row in soup.select('tr.book'):
        book = {}
        book['h3'] = row.find('td', class_='h3g').get_text(strip=True)
        book['star-rating'] = row.find('td', class_='star-rating').get_text(strip=True)
        book['product_price'] = float(row.find('td', class_='product_price').get_text(strip=True))
        book.append(book)
    
    return books

# Scrape the first 10 pages
all_books = []
for page_num in range(1, 11):
    all.books(scrape_page(page_num))


# Create a DataFrame to display the books
df_books = pd.DataFrame(all_books, columns=['star-rating', 'title', 'product_price'])
print(df_books)

# Scrape the first 10 pages for positive goal differential
positive_diff_books = []
for page_num in range(1, 11):
    positive_diff_books.extend([team for team in scrape_page(page_num) if team['goal_diff'] > 0])

# Write to result.csv
df_positive_diff = pd.DataFrame(positive_diff_books, columns=['name', 'year', 'percent', 'goal_diff'])
df_positive_diff.to_csv('result.csv', index=False)
print("Les équipes avec un différentiel positif ont été écrites dans 'result.csv'.")