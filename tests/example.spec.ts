//Я скопировала пример из раздела «Написание тестов» и запустила его
//Этот код открывает сайт playwright.dev, проверяет, что в заголовке вкладки есть слово "Playwright", а потом кликает по ссылке "Get started"
//и проверяет, что открылась страница с заголовком "Installation"
// Время: 22:38
// Дата: 09.11.2026  ФИО: Мамедова Хадижа Садыг кызы
import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('https://playwright.dev/');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/Playwright/);
});

test('get started link', async ({ page }) => {
  await page.goto('https://playwright.dev/');

  // Click the get started link.
  await page.getByRole('link', { name: 'Get started' }).click();

  // Expects page to have a heading with the name of Installation.
  await expect(page.getByRole('heading', { name: 'Installation' })).toBeVisible();
});
