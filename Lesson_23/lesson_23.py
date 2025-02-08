from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)

def test_id_name(driver):
    input_data = 'jejejeje'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    #text_string = driver.find_element(By.ID, 'id_text_string')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    #text_string.submit()
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data


def test_class_name(driver):
    input_data = 'jejejeje'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.CLASS_NAME, 'textinput')
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.CLASS_NAME, 'result-text')
    assert result_text.text == input_data


def test_tag_name(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Input field'

def test_link(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    #contact_link = driver.find_element(By.LINK_TEXT, 'Contact')
    contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'act')
    contact_link.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Contact us'

def test_css_selector(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    #text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder="Submit me"]')
    text_string = driver.find_element(By.CSS_SELECTOR, '.textinput')
    text_string.send_keys('input_data')
    text_string.send_keys(Keys.ENTER)
