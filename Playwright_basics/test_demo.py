from dataclasses import field

from playwright.sync_api import Page, expect
import re
from time import sleep


def test_first(page: Page):
    sleep(3)
    page.goto('https://www.google.com/')
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    search_field.press('Enter')
    expect(page).to_have_title(re.compile('^cat'))


def test_by_role(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.get_by_role('menuitem', name="What's New").click()
    sleep(3)
    page.get_by_role('link', name="Search Terms").click()
    sleep(3)


def test_by_text(page: Page):
    page.goto('https://www.qa-practice.com/')
    page.get_by_text('Single UI Elements').click()
    sleep(3)


def test_by_label(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    field = page.get_by_label('Text string')
    sleep(3)
    field.press_sequentially('1221123c', delay=0.2)
    sleep(1)
    field.press('Control+a')
    sleep(1)
    field.press('Backspace')
    sleep(3)


def test_by_placeholder(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    page.get_by_placeholder('Submit me').fill('dsfs3433')
    sleep(3)


def test_by_alt_text(page: Page):
    sleep(3)
    page.goto('https://trinixy.ru/')
    page.get_by_alt_text('Родители решили показать своим детям мир').click()
    sleep(3)


def test_by_title(page: Page):
    page.goto('https://www.google.com/')
    field = page.get_by_title('Search')
    field.press_sequentially('cat')
    sleep(1)
    field.press('Control+a')
    sleep(1)
    field.press('Backspace')
    sleep(3)


def test_by_testid(page: Page):
    page.goto('https://www.airbnb.ru/')
    sleep(3)
    page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()
    sleep(3)


def test_by_css_selector(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    sleep(3)
    page.locator('.showcart').click()
    sleep(3)


def test_by_xpath(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.locator('//*[@class="action showcart"]').click()
    sleep(3)

