#фио: Мамедова Хадижа Садыг кызы 
#дата: 15.11.26
#время: 21:41
#описание: тест перехватывает запрос к API сайту,подменяет ответ и проверяет,что на странице появился текст "Strawberry"
# описание изменений:
# Вместо одного фрукта, я возвращаю целый список из трех разных фруктов (Яблоко, Банан, Апельсин)
# Я проверяю, что на странице отображаются все три фрукта, а не один.

from playwright.sync_api import Page, expect, Route

def test_mock_the_fruit_api(page: Page):
    def handle(route: Route):
        # Возвращаем список из трех фруктов
        json = [
            {"name": "Apple", "id": 1},
            {"name": "Banana", "id": 2},
            {"name": "Orange", "id": 3}
        ]
        route.fulfill(json=json)

    # Перехватываем запрос к API
    page.route("*/**/api/v1/fruits", handle)

    # Переходим на страницу
    page.goto("https://demo.playwright.dev/api-mocking")

    # Проверяем, что на странице есть все три фрукта
    expect(page.get_by_text("Apple")).to_be_visible()
    expect(page.get_by_text("Banana")).to_be_visible()
    expect(page.get_by_text("Orange")).to_be_visible()