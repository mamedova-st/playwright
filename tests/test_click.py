#фио: Мамедова Хадижа Садыг кызы 
#дата: 15.11.26
#время: 23:34
#описание: открывает гугл карты на эмуляторе Pixel 7, закрывает окно, имитирует свайп карты с помощью touch  и делает скрин
#описание изменений :
# 1. В оригинале тест падал, так как кнопка "Keep using web" не появлялась. Я убрала клик по этой кнопке, чтобы тест не зависал.
# 2. Я изменила координаты свайпа (вместо 200, 100 на 300, 150).
# 3. Добавила print, чтобы видеть результат в консоли.

from playwright.sync_api import sync_playwright, expect

def pan(locator, deltaX=0, deltaY=0, steps=10):
    bounds = locator.bounding_box()
    centerX = bounds['x'] + bounds['width'] / 2
    centerY = bounds['y'] + bounds['height'] / 2

    touches = [{'identifier': 0, 'clientX': centerX, 'clientY': centerY}]
    locator.dispatch_event('touchstart', {
        'touches': touches, 'changedTouches': touches, 'targetTouches': touches
    })

    for i in range(1, steps + 1):
        touches = [{
            'identifier': 0,
            'clientX': centerX + deltaX * i / steps,
            'clientY': centerY + deltaY * i / steps,
        }]
        locator.dispatch_event('touchmove', {
            'touches': touches, 'changedTouches': touches, 'targetTouches': touches
        })

    locator.dispatch_event('touchend')

def test_pan_gesture_to_move_the_map(page):
    page.goto('https://www.google.com/maps/place/@37.4117722,-122.0713234,15z', wait_until='commit')
     
    
    met = page.locator('[data-test-id="met"]')
    
    for _ in range(5):
        pan(met, 300, 150) 
        
    page.screenshot(path="screenshot.png")
    print("Свайп выполнен! Скриншот сохранен.")

# Запуск скрипта
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(**p.devices['Pixel 7'])
    page = context.new_page()
    test_pan_gesture_to_move_the_map(page)
    browser.close()