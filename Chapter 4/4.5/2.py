import requests
from bs4 import BeautifulSoup

url = "https://www.metmuseum.org/art/collection/search/436535" 
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
span_class = "artwork-tombstone--value"
name_tag = soup.find_all("span", class_= span_class) 

print(name_tag[1].parent.text)