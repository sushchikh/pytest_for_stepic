import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="es", help="option: es or fr, etc..."
    )


@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("--language")


@pytest.fixture(scope="function")
def browser():
    print("\nСтартуем браузер")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nЗакрываем браузер")
    browser.quit()