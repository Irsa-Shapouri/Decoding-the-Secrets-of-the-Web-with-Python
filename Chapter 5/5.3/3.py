#Selenium Verision > = 4:

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://github.com/trending")

element = driver.find_element(By.TAG_NAME, "article")
name = driver.find_element(By.CLASS_NAME, "h3.lh-condensed")

print(name.text)


#Selenium Verision < 3:

element = driver.find_element_by_tag_name("article")
name = element.find_element_by_class_name("h3.lh-condensed")



#Selenium Verision > = 4:

try:
    name = "danielmiessler / fabric"
    driver.find_element(By.LINK_TEXT, name)
    print("The project is still in the trending list.")

except:
    print("The project is not in the trending list.")


#Selenium Verision < 3:
    
driver.get("https://github.com/trending")
try:
    name = "danielmiessler / fabric"
    driver.find_element_by_link_text(name)
    print("The project is still in the trending list.")

except:
    print("The project is not in the trending list.")


#Selenium Verision > = 4:

projects = driver.find_elements(By.PARTIAL_LINK_TEXT, "Chat")

for project in projects:
    print(project.text)


#Selenium Verision < 3:

projects = driver.find_elements_by_partial_link_text("Chat")

for project in projects:
    print(project.text)