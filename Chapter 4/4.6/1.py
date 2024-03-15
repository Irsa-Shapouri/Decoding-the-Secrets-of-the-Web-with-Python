import requests
from bs4 import BeautifulSoup

url = "https://www.ikea.com/us/en/cat/products-products/" 
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
div_class = "vn-p-grid-gap vn-accordion__item" 
main_container = soup.find_all("div", class_ = div_class)

ul_class = "vn-list--plain vn-list vn-accordion__content" 
item_list = main_container[18].find("ul", class_ = ul_class)
items = item_list.contents

for item in items: 
    print(item.text)