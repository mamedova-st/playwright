#фио: Мамедова Хадижа Садыг кызы
#дата: 15.11.26
#время: 21:18
#описание: создает два разных окна внутри одного запуска
# ОПИСАНИЕ ИЗМЕНЕНИЙ:
# Я добавила переход на сайты в каждом окне, чтобы проверить, что они работают независимо
# В первом окне открывается Википедия, во втором — Playwright

from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    # Создаем браузер
    chromium = playwright.chromium
    browser = chromium.launch()

    # Создаем два изолированных контекста
    user_context = browser.new_context()
    admin_context = browser.new_context()

    # Создаем страницы и взаимодействуем с ними независимо
    #  Добавляем переходы на сайты
    page1 = user_context.new_page()
    page1.goto("https://www.wikipedia.org/")
    print("Первое окно открыло Википедию")

    page2 = admin_context.new_page()
    page2.goto("https://playwright.dev/")
    print("Второе окно открыло Playwright")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)