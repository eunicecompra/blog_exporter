from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

driver = webdriver.Remote("http://localhost:4444/wd/hub", DesiredCapabilities.CHROME)
driver.get("http://inanywhereelse.blogspot.com/")
assert driver.title.rfind("In Anywhere Else") != -1

# elements = driver.find_elements_by_xpath("//a[contains(@href, '/2010/05/')]")
# /assert len(elements) > 0
elements = driver.find_elements_by_class_name("toggle")
print(f"Number of elements {len(elements)}")
for element in elements:
    print(f"Tag name: " + element.tag_name)
    if "a" == element.tag_name:
        print("waiting for 5 seconds")
        driver.implicitly_wait(5)
        element.click()

driver.close()
