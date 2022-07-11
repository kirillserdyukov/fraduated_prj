import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import fake_useragent

# user = fake_useragent.UserAgent().random


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser")
    option = Options()
    option.binary_location = "/usr/bin/google-chrome"
    # option.add_argument('disable-notifications')  # выключаем оповещения
    option.add_argument('--no-sandbox')
    option.add_argument('--headless')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument("--start-maximized")
    # option.add_argument(f"user-agent={user}")
    option.add_argument("--check-box")# подменить user-agent
    driver = webdriver.Chrome(options=option)
    # driver.maximize_window()
    yield driver
    print("\nquit browser")
    driver.quit()
