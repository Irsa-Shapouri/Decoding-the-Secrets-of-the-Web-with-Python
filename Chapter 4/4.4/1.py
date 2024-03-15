import requests
from bs4 import BeautifulSoup

url = "https://www.spacex.com/vehicles/dragon/" 
response = requests.get(url)

html = response.content
soup = BeautifulSoup(html, "html.parser") 
Specifications = soup.find("tbody") 

print(Specifications.text)