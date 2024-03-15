
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://news.ycombinator.com/")

xpath = '//span[@class="titleline"]/a'
links = driver.find_elements(By.XPATH, xpath)

for link in links:
    print(link.get_attribute("href"))