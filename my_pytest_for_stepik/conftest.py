# импорты
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """
    Получаем из командной строки параметр языка (fr, es, ru, и т.п.)
    """
    parser.addoption(
        "--language", action="store", default="es", help="option: es or fr, etc..."
    )


@pytest.fixture(scope="function")
def language(request):
    """
    Передаем параемтр языка в тесты, чтобы они запускались с разными языками
    """
    return request.config.getoption("--language")


@pytest.fixture(scope="function")
def browser():
    """
    Передаем параметр браузера, в данном случае Хром. Задаем допустимое ожидание элментемнов на странице (5 сек).
    Автоматически закрываем браузер.
    """
    print("\nСтартуем браузер")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nЗакрываем браузер")
    browser.quit()