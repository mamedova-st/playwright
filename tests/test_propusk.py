#фио: Мамедова Хадижа Садыг кызы
#дата: 14.11.26
#время: 17:43
#описание: этот тест открывает сайт и указывает что в браузере firefox его запускать не нужно
#я изменила исходный пример
#поменяла сайт на википедию и добавила проверу заголовка(assert)
#тест будет пропущен в Firefox
import pytest
from playwright.sync_api import Page

@pytest.mark.skip_browser("firefox")
def test_visit_example(page: Page):
    page.goto("https://www.wikipedia.org/")
    assert "Wikipedia" in page.title()