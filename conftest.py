import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import fake_useragent

# user = fake_useragent.UserAgent().random


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser")
    option = Options()
    option.binary_location = "/usr/bin/google-chrome" # для тестов внутри контейнера
    option.add_argument('disable-notifications')  # выключаем оповещения
    option.add_argument('--no-sandbox')
    option.add_argument('--headless')
    option.add_argument('--disable-dev-shm-usage')
    # option.add_argument('--allow-file-access-from-files')
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--start-maximized")
    # option.add_argument(f"user-agent={user}") # подменить user-agent
    option.add_argument("--check-box")
    driver = webdriver.Chrome(options=option)
    # driver.set_window_rect(x=None, y=None, width=1920, height=1080)
    yield driver
    print("\nquit browser")
    driver.quit()
