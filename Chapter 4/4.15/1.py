import requests
from bs4 import BeautifulSoup

url = 'https://www.goodreads.com/list/show/1.Best_Books_Ever'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

books = soup.select('a.bookTitle')[:5]

for book in books:
    title = book.select_one('span')
    print(title.text)