import json
import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local",
            "account": ""
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState),
           'savefile.default_directory': 'output'}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', profile)
chrome_options.add_argument('--kiosk-printing')
driver = webdriver.Chrome(executable_path=os.environ.get('DRIVER_EXECUTABLE'), options=chrome_options)


def launch(web_url):
    driver.get(web_url)
    return driver.title


def toggle_posts():
    print("Toggle all posts...")
    elements = driver.find_elements_by_class_name("toggle")
    for element in elements:
        if element.is_displayed():
            element.click()


def list_posts():
    print("Get all posts...")
    blog_posts = []
    elements = driver.find_elements_by_class_name("posts")
    for element in elements:
        li_elements = element.find_elements_by_tag_name("li")
        for li in li_elements:
            blog_posts.append(li.find_element_by_tag_name("a").get_attribute('href'))

    return blog_posts


def save_as_pdf(blog_posts):
    x = 0
    for post in blog_posts:
        x += 1
        print(f"Saving [{x}] {post}")
        launch(post)
        driver.execute_script('window.print();')
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        WebDriverWait(driver, 180).until(EC.number_of_windows_to_be(1))


def close():
    driver.quit()
