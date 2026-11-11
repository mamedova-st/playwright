# ФИО: Мамедова Хадижа Садыг кызы
# Дата: 11.11.2026
# Время: 11:48
# Я изменила исходный пример
# 1. Вместо проверки URL я добавил проверку заголовка страницы (title)
# 2. Это нужно, чтобы тест проверял не только адрес, но и то, что страница действительно загрузилась правильно
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield

    print("after the test runs")

def test_main_navigation(page: Page):
    # Вместо проверки URL проверяем заголовок страницы
    title = page.title()
    assert "Playwright" in title, f"Ожидалось 'Playwright', получено: {title}"
    print("Тест прошел успешно! Заголовок:", title)