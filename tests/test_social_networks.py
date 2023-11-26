from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_twitter_link_header():
    driver.get("https://www.agoramodels.com/")

    time.sleep(3)

    twitter = driver.find_element(By.XPATH, '//*[@id="prenav"]/div[2]/div/div/div[1]/ul/li[1]/a')
    twitter.click()

    time.sleep(3)

    assert driver.current_url == "https://twitter.com/AgoraModels"


def test_link_facebook_header():
    driver.get("https://www.agoramodels.com/")

    time.sleep(3)

    twitter = driver.find_element(By.XPATH, '//*[@id="prenav"]/div[2]/div/div/div[1]/ul/li[2]/a')
    twitter.click()

    time.sleep(3)

    assert driver.current_url == "https://www.facebook.com/AgoraModelsOfficial/"


def test_link_youtube_header():
    driver.get("https://www.agoramodels.com/")

    time.sleep(3)

    twitter = driver.find_element(By.XPATH, '//*[@id="prenav"]/div[2]/div/div/div[1]/ul/li[3]/a')
    twitter.click()

    time.sleep(3)

    assert driver.current_url == "https://www.youtube.com/AgoraModels"


def test_link_instagram_header():
    driver.get("https://www.agoramodels.com/")

    time.sleep(3)

    twitter = driver.find_element(By.XPATH, '//*[@id="prenav"]/div[2]/div/div/div[1]/ul/li[4]/a')
    twitter.click()

    time.sleep(3)

    assert driver.current_url == "https://www.instagram.com/agoramodels/"


    driver.quit()

