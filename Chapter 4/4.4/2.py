from bs4 import BeautifulSoup 
import requests

url = "https://coinmarketcap.com/currencies/bitcoin" 
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser") 
data = soup.find("div", id = "section-coin-overview")

print(data.text)