from selenium import webdriver

driver = webdriver.Chrome()

url = "https://www.python.org/"
driver.get(url)
url = "https://www.selenium.dev/"
driver.get(url)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

driver.close()