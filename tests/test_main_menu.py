from selenium.webdriver.support import expected_conditions as EC
from locators import MAIN_PAGE_BUTTON, MAIN_PAGE, MODEL_TALK_PAGE, MODEL_TALK_BUTTON, EXPERTS_PAGE, EXPERTS_BUTTON, DOWNLOAD_PAGE, DOWNLOAD_BUTTON, MY_ACCOUNT_BUTTON, MY_ACCOUNT_PAGE, FORUM_PAGE, FORUM_BUTTON, SUPPORT_PAGE, SUPPORT_BUTTON


def test_start_page(driver, open_website, wait):
    start_page = wait.until(EC.element_to_be_clickable(MAIN_PAGE_BUTTON))
    start_page.click()

    assert driver.current_url == MAIN_PAGE


def test_model_talk(driver, open_website, wait):
    model_talk = wait.until(EC.element_to_be_clickable(MODEL_TALK_BUTTON))
    model_talk.click()

    assert driver.current_url == MODEL_TALK_PAGE


def test_experts(driver, open_website, wait):
    experts = wait.until(EC.element_to_be_clickable(EXPERTS_BUTTON))
    experts.click()

    assert driver.current_url == EXPERTS_PAGE


def test_download(driver, open_website, wait):
    download = wait.until(EC.element_to_be_clickable(DOWNLOAD_BUTTON))
    download.click()

    assert driver.current_url == DOWNLOAD_PAGE


def test_my_account(driver, open_website, wait):
    my_acc = wait.until(EC.element_to_be_clickable(MY_ACCOUNT_BUTTON))
    my_acc.click()

    assert driver.current_url == MY_ACCOUNT_PAGE


def test_forum(driver, open_website, wait):
    forum = wait.until(EC.element_to_be_clickable(FORUM_BUTTON))
    forum.click()

    assert driver.current_url == FORUM_PAGE


def test_support(driver, open_website, wait):
    support = wait.until(EC.element_to_be_clickable(SUPPORT_BUTTON))
    support.click()

    assert driver.current_url == SUPPORT_PAGE