from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep
from selenium.webdriver.remote.webelement import WebElement



@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_new_tab(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    driver.find_element(By.ID, 'new-page-link').click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == 'I am a new page in a new tab'
    driver.close()
    driver.switch_to.window(tabs[0])


def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    burger_menu = driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon')
    burger_menu.click()
    sleep(2)
    driver.switch_to.default_content()
    driver.find_element(By.LINK_TEXT, 'Iframe')


def test_stale_exception(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    print(checkbox.id)
    checkbox.click()
    submit = driver.find_element(By.ID, 'submit-id-submit')
    print(submit.id)
    submit.click()
    assert driver.find_element(By.ID, 'result-text').text == 'select me or not'
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    checkbox.click()
    submit = driver.find_element(By.ID, 'submit-id-submit')
    submit.click()


def test_drop_menu(driver):
    driver.implicitly_wait(10)
    driver.get('https://magento.softwaretestingboard.com/')
    privacy = driver.find_element(By.CSS_SELECTOR, 'button[mode="primary"]')
    # wait = WebDriverWait(driver, 5)
    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[mode="primary"] span')))
    privacy.click()
    women = driver.find_element(By.ID, 'ui-id-4')
    tops = driver.find_element(By.ID, 'ui-id-9')
    jackets = driver.find_element(By.ID, 'ui-id-11')
    #ActionChains(driver).move_to_element(women).move_to_element(tops).click(jackets).perform()
    actions = ActionChains(driver)
    actions.move_to_element(women)
    actions.move_to_element(tops)
    actions.click(jackets)
    actions.perform()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Jackets'


def test_d_n_d(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    first = driver.find_element(By.ID, 'rect-draggable')
    second = driver.find_element(By.ID, 'rect-droppable')
    #ActionChains(driver).drag_and_drop(first, second).perform()
    actions = ActionChains(driver)
    actions.click_and_hold(first)
    actions.move_to_element(second)
    actions.release()
    actions.perform()


def test_open_in_new_tab(driver):
    driver.get('https://www.qa-practice.com/')
    link = driver.find_element(By.LINK_TEXT, 'Homepage')
    ActionChains(driver).key_down(Keys.COMMAND).click(link).key_up(Keys.COMMAND).perform()


def test_alert(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element(By.CLASS_NAME, 'a-button').click()
    alert = Alert(driver)
    alert.accept()