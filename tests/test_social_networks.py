# import pytest
# from selenium import webdriver
from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locators import TWITTER_BUTTON_HEADER, MAIN_PAGE, TWITTER_PAGE, FACEBOOK_BUTTON_HEADER, FACEBOOK_PAGE, YOUTUBE_BUTTON_HEADER, YOUTUBE_ACCEPT_BUTTON, YOUTUBE_PAGE, INSTAGRAM_BUTTON_HEADER, INSTAGRAM_PAGE, TWITTER_BUTTON_FOOTER, FACEBOOK_BUTTON_FOOTER, YOUTUBE_BUTTON_FOOTER, INSTAGRAM_BUTTON_FOOTER, TWITTER_LOAD, FACEBOOK_LOAD, YOUTUBE_LOAD, INSTAGRAM_LOAD


def test_twitter_link_header(driver, open_website, wait):

    twitter = wait.until(EC.element_to_be_clickable(TWITTER_BUTTON_HEADER))
    twitter.click()

    load = wait.until(EC.presence_of_all_elements_located(TWITTER_LOAD))

    assert driver.current_url == TWITTER_PAGE


def test_link_facebook_header(driver, open_website, wait):

    facebook = wait.until(EC.element_to_be_clickable(FACEBOOK_BUTTON_HEADER)).click()

    load = wait.until(EC.presence_of_all_elements_located(FACEBOOK_LOAD))

    assert driver.current_url == FACEBOOK_PAGE


def test_link_youtube_header(driver, open_website, wait):

    youtube = wait.until(EC.element_to_be_clickable(YOUTUBE_BUTTON_HEADER)).click()

    button_accept_cookies = wait.until(EC.element_to_be_clickable(YOUTUBE_ACCEPT_BUTTON))
    ActionChains(driver)\
         .scroll_to_element(button_accept_cookies)\
         .perform()

    button_accept_cookies.click()

    load = wait.until(EC.presence_of_all_elements_located(YOUTUBE_LOAD))

    assert driver.current_url == YOUTUBE_PAGE


def test_link_instagram_header(driver, open_website, wait):

    instagram = wait.until(EC.element_to_be_clickable(INSTAGRAM_BUTTON_HEADER)).click()

    load = wait.until(EC.presence_of_all_elements_located(INSTAGRAM_LOAD))

    assert driver.current_url == INSTAGRAM_PAGE


def test_twitter_link_footer(driver, open_website, wait):
    twitter = wait.until(EC.element_to_be_clickable(TWITTER_BUTTON_HEADER))

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    footer_twitter = wait.until(EC.element_to_be_clickable(TWITTER_BUTTON_FOOTER))
    time.sleep(1)
    footer_twitter.click()

    load = wait.until(EC.presence_of_all_elements_located(TWITTER_LOAD))

    assert driver.current_url == TWITTER_PAGE


def test_facebook_link_footer(driver, open_website, wait):

    facebook = wait.until(EC.element_to_be_clickable(FACEBOOK_BUTTON_HEADER))

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    footer_facebook = wait.until(EC.element_to_be_clickable(FACEBOOK_BUTTON_FOOTER))
    time.sleep(1)
    footer_facebook.click()

    load = wait.until(EC.presence_of_all_elements_located(FACEBOOK_LOAD))

    assert driver.current_url == FACEBOOK_PAGE


def test_youtube_link_footer(driver, open_website, wait):

    youtube = wait.until(EC.element_to_be_clickable(YOUTUBE_BUTTON_HEADER))

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    footer_youtube = wait.until(EC.element_to_be_clickable(YOUTUBE_BUTTON_FOOTER))
    time.sleep(1)
    footer_youtube.click()

    button_accept_cookies = wait.until(EC.element_to_be_clickable(YOUTUBE_ACCEPT_BUTTON))
    ActionChains(driver) \
        .scroll_to_element(button_accept_cookies) \
        .perform()

    button_accept_cookies.click()

    load = wait.until(EC.presence_of_all_elements_located(YOUTUBE_LOAD))

    assert driver.current_url == YOUTUBE_PAGE


def test_instagram_link_footer(driver, open_website, wait):
    instagram = wait.until(EC.element_to_be_clickable(INSTAGRAM_BUTTON_HEADER))

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    footer_instagram = wait.until(EC.element_to_be_clickable(INSTAGRAM_BUTTON_FOOTER))
    time.sleep(1)
    footer_instagram.click()

    load = wait.until(EC.presence_of_all_elements_located(INSTAGRAM_LOAD))

    assert driver.current_url == INSTAGRAM_PAGE


