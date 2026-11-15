#фио: Мамедова Хадижа Садыг кызы
#дата: 15.11.26
#время: 22:20
#описание: тест перехватывает запрос к API,получает список  фруктов,добавляет к нему "Loquat" и проверяет, что она появилась на странице
# описание изменений:
# Добавила строчку импорта в самом верху (в оригинале её не было, и код падал с ошибкой)
# Вместо мушмулы я добавила два новых фрукта: Манго и Ананас 
# я проверяю, что на странице отображается заголовок "Render a List of Fruits"

from playwright.sync_api import Page, expect, Route

def test_gets_the_json_from_api_and_adds_a_new_fruit(page: Page):
    def handle(route: Route):
        response = route.fetch()
        json = response.json()
        
        # Добавляем Манго и Ананас
        json.append({"name": "Mango", "id": 777})
        json.append({"name": "Pineapple", "id": 888})
        
        # Отправляем измененный ответ
        route.fulfill(response=response, json=json)

    # Перехватываем запрос к API
    page.route("https://demo.playwright.dev/api-mocking/api/v1/fruits", handle)

    # Переходим на страницу
    page.goto("https://demo.playwright.dev/api-mocking")

    # Проверяем, что страница загрузилась и заголовок на месте
    expect(page.get_by_role("heading", name="Render a List of Fruits")).to_be_visible()