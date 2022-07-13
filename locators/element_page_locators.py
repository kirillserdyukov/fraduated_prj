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


class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "#addNewRecordButton")
    FIRSTNAME_FIELD = (By.CSS_SELECTOR, "#firstName")
    LASTNAME_FIELD = (By.CSS_SELECTOR, "#lastName")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#userEmail")
    AGE_FIELD = (By.CSS_SELECTOR, "#age")
    SALARY_FIELD = (By.CSS_SELECTOR, "#salary")
    DEPARTMENT_FIELD = (By.CSS_SELECTOR, "#department")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")

    ROWS_IN_TABLE = (By.CSS_SELECTOR, "div.rt-tr-group")
    ROWS_COUNT_LIST = (By.CSS_SELECTOR, "div.rt-tr-group")


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "#doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "#rightClickBtn")
    LEFT_CLICK_BUTTON = (By.XPATH, "//div[3]/button")
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "#doubleClickMessage")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "#rightClickMessage")
    LEFT_CLICK_MESSAGE = (By.CSS_SELECTOR, "#dynamicClickMessage")


class LinksPageLocators:
    HOME_LINK = (By.CSS_SELECTOR, "#simpleLink")
    BAD_REQUEST = (By.CSS_SELECTOR, "#bad-request")
