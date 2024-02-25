from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from locators import CARS_MODELS, MODELS, LOTUS_LINK, IMAGE_LOTUS_AUTO, ASTON_007_LINK, IMAGE_007_ASTON_AUTO, CORVETTE_LINK, IMAGE_CORVETTE_AUTO, IMAGE_OPTIMUS, IMAGE_COBRA_AUTO, COBRA_LINK, IMAGE_917KH_AUTO, POR_917KH_LINK, LAFERRARI_LINK, IMAGE_LAFERRARI_AUTO, IMAGE_300SL_AUTO, MERC_300SL_LINK, W196R_LINK, IMAGE_W196R_AUTO, IMAGE_ETYPE_AUTO, ETYPE_LINK, FIRETRUCK_LINK, IMAGE_FIRETRUCK_AUTO, SUPERSNAKE_LINK, IMAGE_SUPERSNAKE_AUTO, IMAGE_LEOPARD, IMAGE_007, GTCOLLECT_LINK, IMAGE_GTCOLLECT_AUTO, IMAGE_BOX, IMAGE_TIRES
from selenium.common.exceptions import ElementNotInteractableException


def test_lotus_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_LOTUS_AUTO))
    image.click()

    assert driver.current_url == LOTUS_LINK


def test_aston007_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_007_ASTON_AUTO))
    image.click()

    assert driver.current_url == ASTON_007_LINK


def test_corvette_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_CORVETTE_AUTO))
    image.click()

    assert driver.current_url == CORVETTE_LINK


def test_optimus_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    try:
        image = driver.find_element(*IMAGE_OPTIMUS).click()
    except ElementNotInteractableException:
        pass


def test_cobra_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_COBRA_AUTO))
    image.click()

    assert driver.current_url == COBRA_LINK


def test_917kh_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_917KH_AUTO))
    image.click()

    assert driver.current_url == POR_917KH_LINK


def test_laferrari_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    swipe = driver.find_element(*IMAGE_LAFERRARI_AUTO)
    ActionChains(driver) \
        .move_to_element(swipe) \
        .perform()

    image = wait.until(EC.element_to_be_clickable(IMAGE_LAFERRARI_AUTO))
    image.click()

    assert driver.current_url == LAFERRARI_LINK


def test_merc300sl_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    swipe = driver.find_element(*IMAGE_300SL_AUTO)
    ActionChains(driver) \
        .move_to_element(swipe) \
        .perform()

    image = wait.until(EC.element_to_be_clickable(IMAGE_300SL_AUTO))
    image.click()

    assert driver.current_url == MERC_300SL_LINK


def test_merc196r_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    swipe = driver.find_element(*IMAGE_W196R_AUTO)
    ActionChains(driver) \
        .move_to_element(swipe) \
        .perform()

    image = wait.until(EC.element_to_be_clickable(IMAGE_W196R_AUTO))
    image.click()

    assert driver.current_url == W196R_LINK


def test_etype_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    swipe = driver.find_element(*IMAGE_ETYPE_AUTO)
    ActionChains(driver) \
        .move_to_element(swipe) \
        .perform()

    image = wait.until(EC.element_to_be_clickable(IMAGE_ETYPE_AUTO))
    image.click()

    assert driver.current_url == ETYPE_LINK


def test_firetruck_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    swipe = driver.find_element(*IMAGE_FIRETRUCK_AUTO)
    ActionChains(driver) \
        .move_to_element(swipe) \
        .perform()

    image = wait.until(EC.element_to_be_clickable(IMAGE_FIRETRUCK_AUTO))
    image.click()

    assert driver.current_url == FIRETRUCK_LINK


def test_supersnake_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    swipe = driver.find_element(*IMAGE_SUPERSNAKE_AUTO)
    ActionChains(driver) \
        .move_to_element(swipe) \
        .perform()

    image = wait.until(EC.element_to_be_clickable(IMAGE_SUPERSNAKE_AUTO))
    image.click()

    assert driver.current_url == SUPERSNAKE_LINK


def test_leopard_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    try:
        swipe = driver.find_element(*IMAGE_LEOPARD)
        ActionChains(driver) \
            .move_to_element(swipe) \
            .perform()

        image = wait.until(EC.element_to_be_clickable(IMAGE_LEOPARD)).click()
    except ElementNotInteractableException:
        pass


def test_007_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    try:
        swipe = driver.find_element(*IMAGE_007)
        ActionChains(driver) \
            .move_to_element(swipe) \
            .perform()

        image = wait.until(EC.element_to_be_clickable(IMAGE_007)).click()
    except ElementNotInteractableException:
        pass


def test_gtcollection_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    swipe = driver.find_element(*IMAGE_GTCOLLECT_AUTO)
    ActionChains(driver) \
        .move_to_element(swipe) \
        .perform()

    image = wait.until(EC.element_to_be_clickable(IMAGE_GTCOLLECT_AUTO))
    image.click()

    assert driver.current_url == GTCOLLECT_LINK


def test_box_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    try:
        swipe = driver.find_element(*IMAGE_BOX)
        ActionChains(driver) \
            .move_to_element(swipe) \
            .perform()

        image = wait.until(EC.element_to_be_clickable(IMAGE_BOX)).click()
    except ElementNotInteractableException:
        pass


def test_tires_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    cars_models = wait.until(EC.element_to_be_clickable(CARS_MODELS))
    cars_models.click()

    try:
        swipe = driver.find_element(*IMAGE_TIRES)
        ActionChains(driver) \
            .move_to_element(swipe) \
            .perform()

        image = wait.until(EC.element_to_be_clickable(IMAGE_TIRES)).click()
    except ElementNotInteractableException:
        pass

