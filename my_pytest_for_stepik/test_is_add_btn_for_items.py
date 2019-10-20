# импорты
from time import sleep


def test_add_btn(language, browser):
    """
    Тетс на наличие кнопки 'добавить в корзину' на разных языках
    :param language: передается параметром из фикстуры (см. conftest.py)
    :param browser: передается параметрм из фикстуры (см. conftest.py)
    """
    # в зависимости от языкового параметра получаем нужный url
    link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
    browser.get(link)
    sleep(30)  # на мой взгляд избыточное ожидание, секунд десяти достаточно, чтобы оценить язык кнопки
    # костыль — в переменную пушим количество элементов с классом "btn-add-to-basket", если элемент хотябы 1 - все ок
    btn_submit = len(browser.find_elements_by_class_name('btn-add-to-basket'))
    assert btn_submit > 0, "нет кнопки 'добавить в корзину'"  # если кнопки нет - выхлопнет ассерт

