#фио: Мамедова Хадижа Садыг кызы
#дата: 11.11.2026
#время: 22:14
#описание: я использовала codegen из документации,он на основе моих действий автоматически сгенерировал код(клики, ввод текста)
import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/")
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("выбросить мусор")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("сделать уроки")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("listitem").filter(has_text="выбросить мусор").get_by_label("Toggle Todo").check()
    page.get_by_role("listitem").filter(has_text="сделать уроки").get_by_label("Toggle Todo").check()
