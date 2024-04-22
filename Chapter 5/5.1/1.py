from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")

url = "https://www.python.org/"
driver.get(url)

print(driver.title)
driver.close()