import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from locators import MAIN_PAGE

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--window-size=1024, 820')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def open_website(driver):
    link = driver.get(MAIN_PAGE)
    return link


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait