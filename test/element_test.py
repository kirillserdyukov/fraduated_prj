import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage


class TestTextBox:
    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        text_box_page.write_inside_all_forms()
        text_box_page.check_created_forms()
        time.sleep(10)


class TestCheckBox:
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
        check_box_page.open()
        check_box_page.open_full_items_list()
        check_box_page.click_random_checkbox()
        check_box_page.get_checked_checkbox()
        check_box_page.get_output_selected_title()
        check_box_page.compare_checked_checkbox_with_selected_output_title()
