import time

from locators.element_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    def write_inside_all_forms(self):
        self.element_is_visible(TextBoxPageLocators.FULL_NAME_FIELD).send_keys('abc')
        self.element_is_visible(TextBoxPageLocators.USER_EMAIL_FIELD).send_keys('abc@gmail.com')
        self.element_is_visible(TextBoxPageLocators.CURRENT_ADDRESS_FIELD).send_keys('abc')
        self.element_is_visible(TextBoxPageLocators.PERMAMENT_ADDRESS_FIELD).send_keys('abc')
        self.element_is_visible(TextBoxPageLocators.SUBMIT_BUTTON).click()

    def check_created_forms(self):
        assert self.element_is_present(TextBoxPageLocators.CREATED_FULL_NAME_FIELD).text.split(':')[1] == 'abc'
        assert self.element_is_present(TextBoxPageLocators.CREATED_USER_EMAIL_FIELD).text.split(':')[1] == 'abc@gmail.com'
        assert self.element_is_present(TextBoxPageLocators.CREATED_CURRENT_ADDRESS_FIELD).text.split(':')[1] == 'abc'
        assert self.element_is_present(TextBoxPageLocators.CREATED_PERMAMENT_ADDRESS_FIELD).text.split(':')[1] == 'abc'
