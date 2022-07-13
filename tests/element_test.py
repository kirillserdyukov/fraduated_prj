import time

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, WebTablePage, ButtonsPage, LinksPage


@allure.feature("TextBox")
class TestTextBox:
    @allure.title("Check text_box")
    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        text_box_page.write_inside_all_forms()
        text_box_page.check_created_forms()


@allure.feature("TextBox")
class TestCheckBox:
    @allure.title("Check check_box")
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
        check_box_page.open()
        check_box_page.open_full_items_list()
        check_box_page.click_random_checkbox()
        check_box_page.get_checked_checkbox()
        check_box_page.get_output_selected_title()
        check_box_page.compare_checked_checkbox_with_selected_output_title()


@allure.feature("TextBox")
class TestWebTable:
    @allure.title("Check adding person in web_table")
    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        web_table_page.add_new_person()
        web_table_page.check_added_person()
        web_table_page.is_added_person_in_table()

    @allure.title("Check changing count of row in web_table")
    def test_web_table_change_count_of_row(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        web_table_page.select_up_to_some_rows()


@allure.feature("TestButton")
class TestButton:
    @allure.title("Check different click on the button")
    def test_different_click_on_the_buttons(self, driver):
        buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
        buttons_page.open()
        buttons_page.click_and_check_message_with_templates()


@allure.feature("LinksTest")
class TestLinks:
    @allure.title("Check home link ")
    def test_check_home_link(self, driver):
        links_page = LinksPage(driver, "https://demoqa.com/links")
        links_page.open()
        links_page.check_home_link_in_new_tab()

    @allure.title("Check bad request link")
    def test_bad_request_link(self, driver): #Negative test
        links_page = LinksPage(driver, "https://demoqa.com/links")
        links_page.open()
        links_page.check_bad_request_link()
