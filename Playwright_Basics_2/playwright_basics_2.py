import re
from time import sleep
from playwright.sync_api import Page, expect, BrowserContext, Playwright, Dialog


def test_visible(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    sleep(1)
    reqs = page.locator('#req_text')
    expect(reqs).not_to_be_visible()
    expect(reqs).to_be_hidden()
    page.locator('#req_header').click()
    sleep(1)
    expect(reqs).to_be_visible()
    sleep(2)


def test_enabled_and_select(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/disabled')
    button = page.locator('#submit-id-submit')
    expect(button).to_be_disabled()
    page.locator('#id_select_state').select_option('Enabled')
    expect(button).to_be_enabled()
    expect(button).to_have_text('Submit')
    expect(button).to_contain_text('ubm')
    sleep(2)


def test_value(page: Page):
    text = 'qwert'
    page.goto('https://www.qa-practice.com/elements/input/simple')
    input_field = page.locator('#id_text_string')
    input_field.fill(text)
    expect(input_field, f'input value is not {text}').to_have_value(text)


def test_sort_and_waits(page: Page):
    page.goto('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    first_man = page.locator('.product-item-link').locator('nth=0')
    print(first_man.inner_text())
    page.locator('#sorter').locator('nth=0').select_option('Price')
    expect(page).to_have_url(re.compile('price'))
    print(first_man.inner_text())
    sleep(5)


def test_tabs(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/link')
    link = page.locator('#new-page-link')
    with context.expect_page() as new_page_event:
        link.click()
    sleep(3)
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    new_page.close()
    page.get_by_role('link', name='New tab button').click()
    sleep(3)


def test_hover(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    men = page.locator('#ui-id-5')
    tops = page.locator('#ui-id-17')
    jackets = page.locator('#ui-id-19')
    men.hover()
    tops.hover()
    jackets.click()
    sleep(3)


def test_d_n_d(page: Page):
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_me = page.locator('#rect-draggable')
    drop_here = page.locator('#rect-droppable')
    drag_me.drag_to(drop_here)
    sleep(3)


def test_alert(page: Page):

    def cancel_alert(alert: Dialog):
        print(alert.message)
        print(alert.type)
        alert.dismiss()

    def fill_and_accept(alert: Dialog):
        alert.accept('some text')
    #page.on('dialog', fill_and_accept)
    page.on('dialog', lambda alert: alert.accept('another text'))
    page.goto('https://www.qa-practice.com/elements/alert/prompt')
    page.get_by_role('link', name='Click').click()
    sleep(3)
