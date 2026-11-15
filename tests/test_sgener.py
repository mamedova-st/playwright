#фио: Мамедова Хадижа Садыг кызы
#дата: 15.11.26
#время: 19:29
#описание: тест открывает сайт playwright кликает по ссылке get started проверяет breadcrumbs 
# и вводит слово locator в поиск 
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_label("Breadcrumbs").get_by_role("list")).to_contain_text("Installation")
    expect(page.get_by_label("Search")).to_be_visible()
    page.get_by_label("Search").click()
    page.get_by_placeholder("Search docs").fill("locator")
    expect(page.get_by_placeholder("Search docs")).to_have_value("locator");