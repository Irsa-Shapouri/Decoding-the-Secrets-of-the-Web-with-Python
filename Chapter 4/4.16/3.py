import requests
from bs4 import BeautifulSoup

url = "https://techxplore.com/hi-tech-news/"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14;rv:65.0) Gecko/20100101 Firefox/65.0"

headers = {"user-agent": USER_AGENT}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all("a", class_= "selection-link news-link")

for link in links:
    article_url = link['href']
    print(article_url)