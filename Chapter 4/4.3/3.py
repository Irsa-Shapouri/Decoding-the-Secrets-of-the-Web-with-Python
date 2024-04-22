from bs4 import BeautifulSoup 
import requests

url = "https://www.quantamagazine.org/topics" 
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

div_class = "alpha-numeric-card"
topic = soup.find_all("div", class_= div_class)[8] 
links = topic.find_all("a")

for link in links: 
    print(link['href'])