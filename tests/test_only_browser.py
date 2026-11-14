#фио:Мамедова Хадижа Садыг кызы
#дата: 15.11.2026
#время: 00:06
#описание:этот тест запускает сайт только в chromium
import pytest

@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...