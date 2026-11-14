#фио:Мамедова Хадижа Садыг кызы
#дата: 15.11.2026
#время: 00:09
#описание изменений: поменяла сайт на Playwright,чтоб открывался реальный сайт
import pytest
from playwright.sync_api import Page

@pytest.mark.only_browser("chromium")
def test_visit_example(page: Page):
    page.goto("https://playwright.dev/")