#фио: Мамедова Хадижа Садыг кызы
#дата: 15.11.26
#время: 22:20
#описание: тест перехватывает запрос к API,получает список  фруктов,добавляет к нему "Loquat" и проверяет, что она появилась на странице
from playwright.sync_api import Page, expect, Route
def test_gets_the_json_from_api_and_adds_a_new_fruit(page: Page):
    def handle(route: Route):
        response = route.fetch()
        json = response.json()
        json.append({ "name": "Loquat", "id": 100})
        # Fulfill using the original response, while patching the response body
        # with the given JSON object.
        route.fulfill(response=response, json=json)

    page.route("https://demo.playwright.dev/api-mocking/api/v1/fruits", handle)

    # Go to the page
    page.goto("https://demo.playwright.dev/api-mocking")

    # Assert that the new fruit is visible
    expect(page.get_by_text("Loquat", exact=True)).to_be_visible()