from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

url = "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"

driver.get(url)


name = driver.find_element(By.ID, "name")
email = driver.find_element(By.ID, "email")
mobile = driver.find_element(By.ID, "mobile")
subjects = driver.find_element(By.ID, "subjects")
address = driver.find_element(By.TAG_NAME, "textarea")


name.send_keys("Irsa")
email.send_keys("irsa.shapouri@gmail.com")
mobile.send_keys("3141592653")
subjects.send_keys("Python, Selenium, Web Scraping")
address.send_keys("Tehran-Iran")

xpath = '//div[2]/input[@type="radio"]'
gender = driver.find_element(By.XPATH, xpath).click()

xpath = '//div[2]/input[@type="checkbox"]'
hobbies = driver.find_element(By.XPATH, xpath).click()

date = driver.find_element(By.NAME, "dob")
date.send_keys("03-13-1989")

file = driver.find_element(By.ID, "picture")
path = "Users/irsa/Desktop/Book/Chapter5/picture.png"
file.send_keys(path)


css_selector = "option[value='NCR']"
state = driver.find_element(By.CSS_SELECTOR, css_selector)
state.click()

css_selector = "option[value='Lucknow']"
city = driver.find_element(By.CSS_SELECTOR, css_selector)
city.click()