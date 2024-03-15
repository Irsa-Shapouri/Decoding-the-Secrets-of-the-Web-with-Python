from selenium import webdriver

driver = webdriver.Chrome()

url = "https://github.com/signup"
driver.get(url)

if "Welcome to GitHub!" in driver.page_source:
    print("GitHub Signup Page Opened Successfully!")