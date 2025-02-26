from playwright.sync_api import Page, expect, Request, Response, Route, APIResponse
from time import sleep
import re
from Lesson_21.lesson_21 import response
import json


def test_listen(page: Page):

    def print_request(request: Request):
        print('REQUEST:', request.post_data, request.url)

    page.on('request', print_request)
    page.on('response', lambda response: print('RESPONSE:', response.url, response.status))
    page.goto('https://www.qa-practice.com/')
    page.get_by_role('link', name='Text input').click()
    input_field = page.locator('#id_text_string')
    input_field.fill('ewwerwerf')
    input_field.press('Enter')


def test_catch_response(page: Page):
    page.goto('https://www.airbnb.ru/')
    with page.expect_response(re.compile('autosuggestions')) as response_event:
    #with page.expect_response('**/autosuggestions**') as response_event:
        page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()

    response = response_event.value
    #print(type(response))
    #playwright.sync_api._generated.Response
    #playwright.sync_api._generated.APIResponse
    expect(APIResponse(response)).to_be_ok()
    print(response.url)
    print(response.status)
    response_data = response.json()
    assert response_data['show_nearby'] is False


def test_pogoda(page: Page):

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['bg_snapshot_delay_ms'] = '700'
        body['rc_enable'] = 'n'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    def handle_route2(route: Route):
        url = route.request.url
        url = url.replace('getconfig/', '')
        route.continue_(url=url)
    sleep(3)
    page.route('**/sodar**', handle_route2)
    page.goto('https://trinixy.ru/')
    page.locator('[name="story"]').click()
    sleep(10)


def test_change_request(page: Page):
    def change_req(route: Route):
        url = route.request.url
        print(url)
        url = url.replace('&filter3=15p01', '')
        route.continue_(url=url)
    page.route(re.compile('/product/finder'), change_req)
    page.goto('https://www.samsung.com/au/smartphones/galaxy-z/')
    sleep(2)
    page.locator('[for="checkbox-series15p01"]').click()
    sleep(5)


def test_API(page: Page):
    response = page.request.get('https://jsonplaceholder.typicode.com/posts/42')
    print(response.json(), response.status)
    expect(response).to_be_ok()
    assert response.json()['id'] == 42
    print(type(response))