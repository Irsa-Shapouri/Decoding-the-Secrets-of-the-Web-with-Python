from selenium import webdriver

driver = webdriver.Chrome()

url = "https://github.com/"
driver.get(url)

print(driver.current_url)