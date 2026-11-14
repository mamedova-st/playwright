#фио: Мамедова Хадижа Садыг кызы
#дата: 14.11.26
#время: 17:09
#описание: этот тест открывает два окна браузера имитируя двух разных пользоватлей
#я изменила исходный пример
#вместо example.com я открываю википедию в первом окне и Playwright во втором
#зачем:чтобы показать работу двух независимых сессий
from playwright.sync_api import Page, BrowserContext
from pytest_playwright.pytest_playwright import CreateContextCallback

def test_foo(page: Page, new_context: CreateContextCallback) -> None:
    page.goto("https://www.wikipedia.org/")
    context = new_context()
    page2 = context.new_page()
    page2.goto("https://playwright.dev/")
    # page and page2 are in different contexts