import time
from pages.elements_page import TextBoxPage, CheckBoxPage, WebTablePage


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


class TestWebTable:
    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        web_table_page.add_new_person()
        web_table_page.check_added_person()
        web_table_page.is_added_person_in_table()

    def test_web_table_change_count_of_row(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        web_table_page.select_up_to_some_rows()


