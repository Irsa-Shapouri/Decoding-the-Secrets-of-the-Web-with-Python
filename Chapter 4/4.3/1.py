from bs4 import BeautifulSoup
import requests

url = "https://www.quantamagazine.org/computer-science/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
titles = soup.find_all("h3")

for title in titles:
    print(title.text)