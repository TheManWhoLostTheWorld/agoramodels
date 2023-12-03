from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_twitter_link_header():
    driver.get("https://www.agoramodels.com/")

    time.sleep(3)

    twitter = driver.find_element(By.XPATH, '//div[@class="col-6 col-sm-6"]/ul/li[1]')
    twitter.click()

    time.sleep(3)

    assert driver.current_url == "https://twitter.com/AgoraModels"


def test_link_facebook_header():
    driver.get("https://www.agoramodels.com/")

    time.sleep(3)

    facebook = driver.find_element(By.XPATH, '//div[@class="col-6 col-sm-6"]/ul/li[2]/a').click()

    time.sleep(3)

    assert driver.current_url == "https://www.facebook.com/AgoraModelsOfficial/"


def test_link_youtube_header():
    driver.get("https://www.agoramodels.com/")

    time.sleep(3)

    youtube = driver.find_element(By.XPATH, '//div[@class="col-6 col-sm-6"]/ul/li[3]/a').click()

    time.sleep(3)

    button_accept_cookies = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span')
    ActionChains(driver)\
         .scroll_to_element(button_accept_cookies)\
         .perform()

    button_accept_cookies.click()

    time.sleep(3)

    assert driver.current_url == "https://www.youtube.com/AgoraModels"


def test_link_instagram_header():
    driver.get("https://www.agoramodels.com/")

    time.sleep(3)

    instagram = driver.find_element(By.XPATH, '//div[@class="col-6 col-sm-6"]/ul/li[4]/a').click()

    time.sleep(3)

    assert driver.current_url == "https://www.instagram.com/agoramodels/"


def test_twitter_link_footer():
    driver.get("https://www.agoramodels.com/")

    time.sleep(1)

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    footer_twitter = driver.find_element(By.XPATH, '//div[@id="footer"]/footer/div/div/div[2]/li[1]/a')
    time.sleep(1) #now there is an issue. It should be solved by expected conditions
    footer_twitter.click()

    time.sleep(1)

    assert driver.current_url == "https://twitter.com/AgoraModels"


def test_facebook_link_footer():
    driver.get("https://www.agoramodels.com/")

    time.sleep(1)

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    footer_facebook = driver.find_element(By.XPATH, '//div[@id="footer"]/footer/div/div/div[2]/li[2]/a/i')

    time.sleep(1) #now there is an issue. It should be solved by expected conditions

    footer_facebook.click()

    time.sleep(3)

    assert driver.current_url == "https://www.facebook.com/AgoraModelsOfficial/"


def test_youtube_link_footer():
    driver.get("https://www.agoramodels.com/")

    time.sleep(1)

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    footer_youtube = driver.find_element(By.XPATH, '//div[@id="footer"]/footer/div/div/div[2]/li[3]/a/i')
    time.sleep(1) #now there is an issue. It should be solved by expected conditions
    footer_youtube.click()

    time.sleep(3)

# there is an issue. Need to solve it

    # button_accept_cookies = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/div[3]')
    # ActionChains(driver)\
    #      .scroll_to_element(button_accept_cookies)\
    #      .perform()
    #
    # button_accept_cookies.click()
    #
    # time.sleep(3)
    #SOLVED

    assert driver.current_url == "https://www.youtube.com/AgoraModels"


def test_instagram_link_footer():
    driver.get("https://www.agoramodels.com/")

    time.sleep(1)

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    footer_instagram = driver.find_element(By.XPATH, '//div[@id="footer"]/footer/div/div/div[2]/li[4]/a/i')

    time.sleep(1) #now there is an issue. It should be solved by expected conditions

    footer_instagram.click()

    time.sleep(3)

    assert driver.current_url == "https://www.instagram.com/agoramodels/"

    driver.quit()

