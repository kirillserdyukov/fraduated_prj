import random
import time

import allure
import requests

from generator.generator import person_generator
from locators.element_page_locators import TextBoxPageLocators, CheckBoxPageLocators, WebTablePageLocators, ButtonsPageLocators, LinksPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    person_info = next(person_generator())
    full_name = person_info.full_name
    email = person_info.email
    current_address = person_info.current_address
    permanent_address = person_info.permanent_address

    @allure.step("write in all forms")
    def write_inside_all_forms(self, full_name=full_name, email=email, current_address=current_address, permanent_address=permanent_address):
        self.element_is_visible(TextBoxPageLocators.FULL_NAME_FIELD).send_keys(full_name)
        self.element_is_visible(TextBoxPageLocators.USER_EMAIL_FIELD).send_keys(email)
        self.element_is_visible(TextBoxPageLocators.CURRENT_ADDRESS_FIELD).send_keys(current_address)
        self.element_is_visible(TextBoxPageLocators.PERMANENT_ADDRESS_FIELD).send_keys(permanent_address)
        self.element_is_clickable(TextBoxPageLocators.SUBMIT_BUTTON).click()

    @allure.step("check filled forms")
    def check_created_forms(self, full_name=full_name, email=email, current_address=current_address, permanent_address=permanent_address):
        assert self.element_is_present(TextBoxPageLocators.CREATED_FULL_NAME_FIELD).text.split(':')[1] == full_name, "the full name not correct"
        assert self.element_is_present(TextBoxPageLocators.CREATED_USER_EMAIL_FIELD).text.split(':')[1] == email, "the email not correct"
        assert self.element_is_present(TextBoxPageLocators.CREATED_CURRENT_ADDRESS_FIELD).text.split(':')[1] == current_address, "the current_email not correct"
        assert self.element_is_present(TextBoxPageLocators.CREATED_PERMANENT_ADDRESS_FIELD).text.split(':')[1] == permanent_address, "the permanent_email not correct"


class CheckBoxPage(BasePage):
    @allure.step("open full items list")
    def open_full_items_list(self):
        self.element_is_visible(CheckBoxPageLocators.EXPAND_BUTTON).click()

    @allure.step("click random checkbox")
    def click_random_checkbox(self):
        checkbox_list = self.elements_are_visible(CheckBoxPageLocators.TITLE_ITEMS)
        count = 16
        while count != 0:
            checkbox = checkbox_list[random.randint(1, 16)]
            self.scroll_into_view(checkbox)
            checkbox.click()
            # print(checkbox.text)
            count -= 1

    @allure.step("get checked checkbox")
    def get_checked_checkbox(self):
        checked_list = self.elements_are_present(CheckBoxPageLocators.CHECKED_CHECKBOX)
        data = []
        for checkbox in checked_list:
            title_name = checkbox.find_element(*CheckBoxPageLocators.CHECKED_ITEM)
            data.append(title_name.text.lower().replace(" ", "").replace(".doc", ""))
        return data

    @allure.step("get output selected title")
    def get_output_selected_title(self):
        result_list = self.elements_are_present(CheckBoxPageLocators.RESULT_LIST)
        data = []
        for result in result_list:
            data.append(result.text.lower())
        return data

    @allure.step("compare checked checkbox with selected output title")
    def compare_checked_checkbox_with_selected_output_title(self):
        assert self.get_checked_checkbox() == self.get_output_selected_title(), "selected checkbox dont match with result output"


class WebTablePage(BasePage):
    @allure.step("add new person")
    def add_new_person(self):
        person_info = next(person_generator())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        self.element_is_visible(WebTablePageLocators.ADD_BUTTON).click()
        self.element_is_visible(WebTablePageLocators.FIRSTNAME_FIELD).send_keys(first_name)
        self.element_is_visible(WebTablePageLocators.LASTNAME_FIELD).send_keys(last_name)
        self.element_is_visible(WebTablePageLocators.EMAIL_FIELD).send_keys(email)
        self.element_is_visible(WebTablePageLocators.AGE_FIELD).send_keys(age)
        self.element_is_visible(WebTablePageLocators.SALARY_FIELD).send_keys(salary)
        self.element_is_visible(WebTablePageLocators.DEPARTMENT_FIELD).send_keys(department)
        self.element_is_visible(WebTablePageLocators.SUBMIT_BUTTON).click()
        return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step("check added person")
    def check_added_person(self):
        rows_in_table = self.elements_are_present(WebTablePageLocators.ROWS_IN_TABLE)
        data = []
        for row in rows_in_table:
            data.append(row.text.splitlines())
        return data

    @allure.step("is added person in table?")
    def is_added_person_in_table(self):
        assert self.add_new_person() in self.check_added_person(), "new person isn't in the table"

    @allure.step("select up to some rows")
    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for i in count:
            select_row_button = self.element_is_visible(WebTablePageLocators.ROWS_COUNT_LIST)
            self.scroll_into_view(select_row_button)
            select_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"[value='{i}']")).click()
            data.append(self.check_count_rows())
        assert count == data, "The count rows in the table haven't been changed"

    @allure.step("check count rows")
    def check_count_rows(self):
        list_rows = self.elements_are_present(WebTablePageLocators.ROWS_IN_TABLE)
        return len(list_rows)


class ButtonsPage(BasePage):
    @allure.step("click on different button")
    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.double_click(self.element_is_visible(ButtonsPageLocators.DOUBLE_CLICK_BUTTON))
            return self.message_after_click(ButtonsPageLocators.DOUBLE_CLICK_MESSAGE)

        if type_click == "right":
            self.right_click(self.element_is_visible(ButtonsPageLocators.RIGHT_CLICK_BUTTON))
            return self.message_after_click(ButtonsPageLocators.RIGHT_CLICK_MESSAGE)

        if type_click == "left":
            self.element_is_visible(ButtonsPageLocators.LEFT_CLICK_BUTTON).click()
            return self.message_after_click(ButtonsPageLocators.LEFT_CLICK_MESSAGE)

    @allure.step("message after click")
    def message_after_click(self, locator):
        return self.element_is_present(locator).text

    @allure.step("click and check message with templates")
    def click_and_check_message_with_templates(self):
        clicks_type = ["double", "right", "left"]
        for click in clicks_type:
            message = self.click_on_different_button(click)
            if click == "double":
                assert message == "You have done a double click"
            if click == "right":
                assert message == "You have done a right click"
            if click == "left":
                assert message == "You have done a dynamic click"


class LinksPage(BasePage):
    @allure.step("check home link in new tab")
    def check_home_link_in_new_tab(self):
        working_link = self.element_is_visible(LinksPageLocators.HOME_LINK)
        link_href = working_link.get_attribute('href')
        requests.get(link_href)
        working_link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        url_2 = self.driver.current_url
        assert link_href == url_2, "home link is not working in new tab"

    @allure.step("check bad request link")
    def check_bad_request_link(self):
        first_page_url = requests.get(self.driver.current_url)
        self.element_is_present(LinksPageLocators.BAD_REQUEST).click()
        second_page_url = requests.get(self.driver.current_url)
        status_code = requests.status_codes
        assert first_page_url != second_page_url and status_code not in [200, 201, 204, 301], "bad_request link is working, when is shouldn't "
