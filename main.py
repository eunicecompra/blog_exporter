from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME)
driver.get("http://inanywhereelse.blogspot.com/")
print("taking screenshot...")
driver.save_screenshot("/app/output/blog.png")
driver.close()
