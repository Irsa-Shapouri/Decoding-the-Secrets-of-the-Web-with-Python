from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get("https://stackoverflow.com/")

pattern = r"\bhttps?:\/\/(?:www\.)?instagram\.com\/ ([a-zA-Z0-9_\.]+)\/?\b"

page_source = driver.page_source
matches = re.findall(pattern, page_source)

if matches:
    print("ID found:")
    for match in matches:
        print(match)
else:
    print("No Instagram ID found on the page.")

driver.quit()