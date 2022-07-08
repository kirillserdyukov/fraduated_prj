import time

from generator.generator import person_generator
from locators.element_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    person_info = next(person_generator())
    full_name = person_info.full_name
    email = person_info.email
    current_address = person_info.current_address
    permanent_address = person_info.permanent_address

    def write_inside_all_forms(self, full_name=full_name, email=email, current_address=current_address, permanent_address=permanent_address):
        self.element_is_visible(TextBoxPageLocators.FULL_NAME_FIELD).send_keys(full_name)
        self.element_is_visible(TextBoxPageLocators.USER_EMAIL_FIELD).send_keys(email)
        self.element_is_visible(TextBoxPageLocators.CURRENT_ADDRESS_FIELD).send_keys(current_address)
        self.element_is_visible(TextBoxPageLocators.PERMAMENT_ADDRESS_FIELD).send_keys(permanent_address)
        self.element_is_visible(TextBoxPageLocators.SUBMIT_BUTTON).click()

    def check_created_forms(self, full_name=full_name, email=email, current_address=current_address, permanent_address=permanent_address):
        assert self.element_is_present(TextBoxPageLocators.CREATED_FULL_NAME_FIELD).text.split(':')[1] == full_name, "the full name not correct"
        assert self.element_is_present(TextBoxPageLocators.CREATED_USER_EMAIL_FIELD).text.split(':')[1] == email, "the email not correct"
        assert self.element_is_present(TextBoxPageLocators.CREATED_CURRENT_ADDRESS_FIELD).text.split(':')[1] == current_address, "the current_email not correct"
        assert self.element_is_present(TextBoxPageLocators.CREATED_PERMAMENT_ADDRESS_FIELD).text.split(':')[1] == permanent_address, "the permanent_email not correct"
