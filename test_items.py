import time
from selenium.webdriver.by import By

# Ссылка на проверяемый товар
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
  browser.get(link)

  # Раскомментируйте строку ниже для визуальной проверки языка (критерий peer-review)
  # time.sleep(30)

  # Проверяем наличие кнопки добавления в корзину по уникальному селектору
  add_to_basket_buttons = browser.find_elements(
      By.CSS_SELECTOR, "button.btn-add-to-basket"
  )

  # Assert проверяет, что кнопка присутствует на странице
  assert (
      len(add_to_basket_buttons) > 0
  ), "Кнопка добавления в корзину отсутствует на странице товара!"