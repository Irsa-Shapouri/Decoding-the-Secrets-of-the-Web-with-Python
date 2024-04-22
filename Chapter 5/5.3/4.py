#Selenium Verision > = 4:

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.worldometers.info/")

css_selector = "#c1 > div.counter-heading.inactive-header > span.counter-number > span"

element = driver.find_elements(By.CSS_SELECTOR, css_selector)

print(element.text)


#Selenium Verision < 3:

element = driver.find_element_by_css_selector(css_selector)