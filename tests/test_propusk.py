#фио: Мамедова Хадижа Садыг кызы
#дата: 14.11.26
#время: 17:26
#описание: этот тест открывает сайт и указывает что в браузере firefox его запускать не нужно
import pytest

@pytest.mark.skip_browser("firefox")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...