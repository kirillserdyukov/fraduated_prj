import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import fake_useragent

user = fake_useragent.UserAgent().random


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser")
    option = Options()
    option.add_argument('disable-notifications')  # выключаем оповещения
    option.headless = False  # В фоновом режиме
    option.add_argument("--start-maximized")
    option.add_argument(f"user-agent={user}")  # подменить user-agent
    driver = webdriver.Chrome(options=option)
    # driver.maximize_window()
    yield driver
    print("\nquit browser")
    driver.quit()
