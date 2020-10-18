from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

driver = webdriver.Remote("http://localhost:4444/wd/hub", DesiredCapabilities.CHROME)
driver.get("http://inanywhereelse.blogspot.com/")
assert driver.title.rfind("In Anywhere Else") != -1

elements = driver.find_elements_by_class_name("toggle")
assert len(elements) > 0
for element in elements:
    if element.is_displayed():
        element.click()
