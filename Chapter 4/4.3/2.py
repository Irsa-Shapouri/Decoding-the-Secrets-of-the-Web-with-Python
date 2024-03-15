import requests
from bs4 import BeautifulSoup

url = "https://www.quantamagazine.org/computer-science/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

div_class = "card__excerpt h5 pangram o6 mb4 mt025"
description = soup.find_all("div", class_= div_class)[1]

print(description.text)