#фио: Мамедова Хадижа Садыг кызы
#дата: 14.11.26
#время: 23:18
#описание: этот тест открывает сайт и разрешает запуск теста ТОЛЬКО в браузере Chromium
import pytest

@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...