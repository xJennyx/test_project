from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_scroll(driver):
    driver.get('https://trinixy.ru/')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')


def test_scroll_to_element(driver):
    driver.get('https://the-internet.herokuapp.com/')
    sleep(3)
    link = driver.find_element(By.LINK_TEXT, 'JQuery UI Menus')
    driver.execute_script('arguments[0].scrollIntoView();', link)


def test_upload(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    upload = driver.find_element(By.ID, 'file-upload')
    button = driver.find_element(By.ID, 'file-submit')
    upload.send_keys('/Users/a1111/Downloads/Battletoads_Double_Dragon_-_The_Ultimate_Team_01.png')
    button.click()
