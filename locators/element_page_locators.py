from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME_FIELD = (By.CSS_SELECTOR, '#userName')
    USER_EMAIL_FIELD = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADDRESS_FIELD = (By.CSS_SELECTOR, '#currentAddress')
    PERMANENT_ADDRESS_FIELD = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')

    CREATED_FULL_NAME_FIELD = (By.CSS_SELECTOR, '#output #name')
    CREATED_USER_EMAIL_FIELD = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS_FIELD = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS_FIELD = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_BUTTON = (By.CSS_SELECTOR, 'button.rct-option.rct-option-expand-all')
    COLLAPSE_BUTTON = (By.CSS_SELECTOR, 'button.rct-option.rct-option-collapse-all')
    TITLE_ITEMS = (By.CSS_SELECTOR, 'span.rct-title')
    CHECKED_CHECKBOX = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    CHECKED_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    RESULT_LIST = (By.CSS_SELECTOR, "span.text-success")

    CURRENT_ADDRESS_FIELD = (By.CSS_SELECTOR, '#currentAddress')
    PERMANENT_ADDRESS_FIELD = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')
