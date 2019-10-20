from selenium import webdriver
from time import sleep


def test_add_btn(language, browser):
    link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
    browser.get(link)
    btn_submit = len(browser.find_elements_by_class_name('btn-add-to-basket'))
    assert btn_submit > 0, "нет кнопки 'добавить в корзину'"
    sleep(10)

