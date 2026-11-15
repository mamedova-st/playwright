#фио: Мамедова Хадиж Садыг кызы
#дата: 15.11.26
#время: 23:11
#описание: тест сгенерирвал codegen там используется настройка для эмуляции браузера айфон 13 затем тест открывает сайт Playwright
import pytest
import re
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


def test_example(page: Page) -> None:
    page.goto("https://playwright.dev/")
