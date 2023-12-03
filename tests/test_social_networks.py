import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from locators import TWITTER_BUTTON_HEADER, MAIN_PAGE, TWITTER_PAGE, FACEBOOK_BUTTON_HEADER, FACEBOOK_PAGE, YOUTUBE_BUTTON_HEADER, YOUTUBE_ACCEPT_BUTTON, YOUTUBE_PAGE, INSTAGRAM_BUTTON_HEADER, INSTAGRAM_PAGE, TWITTER_BUTTON_FOOTER, FACEBOOK_BUTTON_FOOTER, YOUTUBE_BUTTON_FOOTER, INSTAGRAM_BUTTON_FOOTER

driver = webdriver.Chrome()


@pytest.fixture(autouse=True)
def open_website():
    return driver.get(MAIN_PAGE)


def test_twitter_link_header():
    time.sleep(3)

    twitter = driver.find_element(By.XPATH, TWITTER_BUTTON_HEADER)
    twitter.click()

    time.sleep(3)

    assert driver.current_url == TWITTER_PAGE


def test_link_facebook_header():
    time.sleep(3)

    facebook = driver.find_element(By.XPATH, FACEBOOK_BUTTON_HEADER).click()

    time.sleep(3)

    assert driver.current_url == FACEBOOK_PAGE


def test_link_youtube_header():
    time.sleep(3)

    youtube = driver.find_element(By.XPATH, YOUTUBE_BUTTON_HEADER).click()

    time.sleep(3)

    button_accept_cookies = driver.find_element(By.XPATH, YOUTUBE_ACCEPT_BUTTON)
    ActionChains(driver)\
         .scroll_to_element(button_accept_cookies)\
         .perform()

    button_accept_cookies.click()

    time.sleep(3)

    assert driver.current_url == YOUTUBE_PAGE


def test_link_instagram_header():
    time.sleep(3)

    instagram = driver.find_element(By.XPATH, INSTAGRAM_BUTTON_HEADER).click()

    time.sleep(3)

    assert driver.current_url == INSTAGRAM_PAGE


def test_twitter_link_footer():
    time.sleep(1)

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    footer_twitter = driver.find_element(By.XPATH, TWITTER_BUTTON_FOOTER)
    time.sleep(1) #now there is an issue. It should be solved by expected conditions
    footer_twitter.click()

    time.sleep(1)

    assert driver.current_url == TWITTER_PAGE


def test_facebook_link_footer():
    time.sleep(1)

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    footer_facebook = driver.find_element(By.XPATH, FACEBOOK_BUTTON_FOOTER)

    time.sleep(1) #now there is an issue. It should be solved by expected conditions

    footer_facebook.click()

    time.sleep(3)

    assert driver.current_url == FACEBOOK_PAGE


def test_youtube_link_footer():
    time.sleep(1)

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    footer_youtube = driver.find_element(By.XPATH, YOUTUBE_BUTTON_FOOTER)
    time.sleep(1) #now there is an issue. It should be solved by expected conditions
    footer_youtube.click()

    time.sleep(3)

    assert driver.current_url == YOUTUBE_PAGE


def test_instagram_link_footer():
    time.sleep(1)

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    footer_instagram = driver.find_element(By.XPATH, INSTAGRAM_BUTTON_FOOTER)

    time.sleep(1) #now there is an issue. It should be solved by expected conditions

    footer_instagram.click()

    time.sleep(3)

    assert driver.current_url == INSTAGRAM_PAGE

    driver.quit()

