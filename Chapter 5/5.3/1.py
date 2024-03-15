#Selenium Verision > = 4:

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://arxiv.org/")

element = driver.find_element(By.ID, "search-category")

driver.quit()


#Selenium Verision < 3:

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://arxiv.org/")

element = driver.find_element_by_id("search-category")

driver.quit()



#Selenium Verision > = 4:

element = driver.find_element(By.NAME, "group")


#Selenium Verision < 3:

element = driver.find_element_by_name("group")