#фио: Мамедова Хадижа Садыг кызы
#дата: 15.11.26
#время: 20:01
#опписание: тест проверяет что элемент с текстом name становится видимым на странице используя тайм-аут в 10 сек.
from playwright.sync_api import expect

def test_foobar(page: Page) -> None:
    expect(page.get_by_text("Name")).to_be_visible(timeout=10_000)