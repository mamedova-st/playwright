# ФИО: Мамедова Хадижа Садыг кызы
# Дата: 10.11.2026
# Время выполнения: 22:37
# Описание изменений: Я взяла пример из документации и изменила его
# 1. Заменила сайт Playwright на Википедию,чтобы работу кода на более сложном тяжелом сайте
# 2. Добавила ожидание загрузки страницы (wait_for_load_state),чтоб тест не падал с ошибкой
# 3. Заменила простой вывод на проверку (assert), что слово "Wikipedia" есть в заголовке,чтоб тест сам выдавал ошибку,если нужного слова нет на странице

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    page.goto("https://www.wikipedia.org/")
    
    page.wait_for_load_state()
    
    title = page.title()
    
    assert "Wikipedia" in title, f"Ожидалось 'Wikipedia', получено: {title}"
    
    print("Всё работает! Заголовок страницы:", title)
    
    browser.close()