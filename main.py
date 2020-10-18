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

elements = driver.find_elements_by_class_name("posts")
assert len(elements) > 0
for element in elements:
    li_elements = element.find_elements_by_tag_name("li")
    for li in li_elements:
        blog_link = li.find_element_by_tag_name("a")
        if blog_link:
            print(blog_link.text)
