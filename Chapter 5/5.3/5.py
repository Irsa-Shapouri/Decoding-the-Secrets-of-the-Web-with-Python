#Selenium Verision > = 4:

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
driver.get(url)

xpath = '//a/h3[@class="ipc-title__text"]'

movies = driver.find_elements(By.XPATH, xpath)

for movie in movies[:5]:
    print(movie.text)


#Selenium Verision < 3:
    
movies = driver.find_elements_by_xpath(xpath)