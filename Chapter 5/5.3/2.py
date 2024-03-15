#Selenium Verision > = 4:

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://news.ycombinator.com/")

element = driver.find_element(By.CLASS_NAME, "titleline")

print(element.text)

driver.quit()


#Selenium Verision < 3:

element = driver.find_element_by_class_name("titleline")



#Selenium Verision > = 4:

driver.get("https://news.ycombinator.com/")

titles = driver.find_elements(By.CLASS_NAME, "titleline")
count = 0

for title in titles:
    print(title.text)
    count += 1
    if count == 5:
        break


#Selenium Verision < 3:

titles = driver.find_elements_by_class_name("titleline")