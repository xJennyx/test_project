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