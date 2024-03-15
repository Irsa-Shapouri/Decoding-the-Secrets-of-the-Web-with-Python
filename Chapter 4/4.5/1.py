import requests
from bs4 import BeautifulSoup

url = "https://www.metmuseum.org/art/collection/search/436535" 
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
name_tag = soup.find("p", class_= "artwork-tombstone--item") 

print(name_tag.parent.text)