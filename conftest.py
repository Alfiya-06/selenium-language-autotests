import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
  # Добавляем считывание параметра --language из командной строки (по умолчанию 'en')
  parser.addoption(
      "--language",
      action="store",
      default="en",
      help="Choose language: es, fr, ru, etc.",
  )


@pytest.fixture(scope="function")
def browser(request):
  # Получаем значение параметра language
  user_language = request.config.getoption("language")

  # Настраиваем опции браузера для передачи нужного языка
  options = Options()
  options.add_experimental_option(
      "prefs", {"intl.accept_languages": user_language}
  )

  print(f"\nЗапуск браузера Chrome с языком: {user_language}...")
  browser = webdriver.Chrome(options=options)
  browser.implicitly_wait(10)

  yield browser

  print("\nЗакрытие браузера...")
  browser.quit()