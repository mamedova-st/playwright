#фио: Мамедова Хадижа Садыг кызы
#дата: 14.11.26
#время: 16:53
#описание: этот тест открывает два окна браузера имитируя двух разных пользоватлей
from playwright.sync_api import Page, BrowserContext
from pytest_playwright.pytest_playwright import CreateContextCallback

def test_foo(page: Page, new_context: CreateContextCallback) -> None:
    page.goto("https://example.com")
    context = new_context()
    page2 = context.new_page()
    # page and page2 are in different contexts