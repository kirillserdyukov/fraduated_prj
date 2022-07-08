from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME_FIELD = (By.CSS_SELECTOR, '#userName')
    USER_EMAIL_FIELD = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADDRESS_FIELD = (By.CSS_SELECTOR, '#currentAddress')
    PERMAMENT_ADDRESS_FIELD = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')

    CREATED_FULL_NAME_FIELD = (By.CSS_SELECTOR, '#output #name')
    CREATED_USER_EMAIL_FIELD = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS_FIELD = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMAMENT_ADDRESS_FIELD = (By.CSS_SELECTOR, '#output #permanentAddress')
