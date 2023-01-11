from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Connecting to the driver
#path_test (str)
def driver_conn(path_test):
    chromedriver_path = path_test
    driver = webdriver.Chrome(service=Service(chromedriver_path))
    return driver

#Connection to URL
#url_test (str)
def get_frontend_test(driver, url_test):
    driver.get(url_test)
    return driver

#Search for an element on the page
def element_test(driver):
    try:
        web_element = driver.find_element(By.ID, value="user_name").text
        return web_element
    except NoSuchElementException:
        raise NoSuchElementException("test failed")
