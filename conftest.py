import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Добавляем обработку командной строки с параметром language
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: ru, en, fr.. etc')

# Описываем фикстуру объявления браузера, который будет передаваться в тестовый метод как параметр
@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options = options)
    yield browser
    browser.quit()