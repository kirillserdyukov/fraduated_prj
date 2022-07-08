import time

from pages.base_page import BasePage
from pages.element_page import TextBoxPage


def test(driver):
    text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    text_box_page.open()
    text_box_page.write_inside_all_forms()
    text_box_page.check_created_forms()

