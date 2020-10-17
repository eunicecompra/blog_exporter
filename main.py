from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME)
driver.get("http://inanywhereelse.blogspot.com/")
driver.get_screenshot_as_png()
driver.close()
