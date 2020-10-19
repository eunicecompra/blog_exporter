from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME)


def launch(web_url):
    driver.get(web_url)
    return driver.title


def toggle_posts():
    elements = driver.find_elements_by_class_name("toggle")
    for element in elements:
        if element.is_displayed():
            element.click()


def list_posts():
    elements = driver.find_elements_by_class_name("posts")
    for element in elements:
        li_elements = element.find_elements_by_tag_name("li")
        for li in li_elements:
            blog_link = li.find_element_by_tag_name("a")
            if blog_link:
                print(blog_link.text)
