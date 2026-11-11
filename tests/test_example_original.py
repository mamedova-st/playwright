#фио:Мамедова Хадижа Садыг кызы
#дата: 11.11.2026
#время: 11:15
#описание: этот код перед тестом автоматически открывает сайт Playwrigth и проверяет что мы находимся именно на этой странице
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
    # Assertions use the expect API.
    expect(page).to_have_url("https://playwright.dev/")