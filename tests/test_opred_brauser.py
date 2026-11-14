#фио: Мамедова Хадижа Садыг кызы
#дата: 14.11.26
#время: 23:55
#описание изменений:поменяла сайт на википедию и добавила проверку заголовка,тест будет запущен в firefox
import pytest
from playwright.sync_api import Page

@pytest.mark.skip_browser("firefox")
def test_visit_example(page: Page):
    page.goto("https://www.wikipedia.org/")
    assert "Wikipedia" in page.title()