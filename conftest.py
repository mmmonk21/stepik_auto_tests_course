import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language", default="en")  # Получаем язык из параметров командной строки

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose language: en, ru, etc.")