#фио: Мамедова Хадижа Садыг кызы
#дата: 15.11.26
#время: 19:43
#описание: тест открывает сайт playwright кликает по ссылке get started проверяет breadcrumbs 
# и вводит слово locator в поиск 
# ОПИСАНИЕ ИЗМЕНЕНИЙ:
# 1. Заменила сайт Playwright на Википедию.
# 2. Вместо клика по ссылке "Get started", я написала проверку, что в строке поиска можно ввести текст "Python", а затем проверила, что этот текст там действительно появился (использовала expect(to_have_value)).

from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    # Переходим на Википедию
    page.goto("https://www.wikipedia.org/")
    
    # Проверяем, что строка поиска видна на странице
    expect(page.get_by_role("searchbox")).to_be_visible()
    
    # Вводим текст в строку поиска
    page.get_by_role("searchbox").fill("Python")
    
    # Проверяем, что в строке поиска теперь написано "Python"
    expect(page.get_by_role("searchbox")).to_have_value("Python")