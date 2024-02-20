from selenium.webdriver.support import expected_conditions as EC
from locators import ALL_MODELS, MODELS, LOTUS_LINK, IMAGE_LOTUS, ASTON_007_LINK, IMAGE_007_ASTON, CORVETTE_LINK, IMAGE_CORVETTE, OPTIMUS_LINK, IMAGE_OPTIMUS, IMAGE_COBRA, COBRA_LINK, IMAGE_917KH, POR_917KH_LINK, LAFERRARI_LINK, IMAGE_LAFERRARI, SLIDER_BUTTON_2, IMAGE_300SL, MERC_300SL_LINK, W196R_LINK, IMAGE_W196R, IMAGE_ETYPE, ETYPE_LINK, SLIDER_BUTTON_3, FIRETRUCK_LINK, IMAGE_FIRETRUCK, SUPERSNAKE_LINK, IMAGE_SUPERSNAKE, LEOPARD_LINK, IMAGE_LEOPARD, SLIDER_BUTTON_4, IMAGE_007, LINK_007, GTCOLLECT_LINK, IMAGE_GTCOLLECT, BOX_LINK, IMAGE_BOX, TIRES_LINK, IMAGE_TIRES
import time


def test_lotus_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_LOTUS))
    image.click()

    assert driver.current_url == LOTUS_LINK


def test_aston007_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_007_ASTON))
    image.click()

    assert driver.current_url == ASTON_007_LINK


def test_corvette_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_CORVETTE))
    image.click()

    assert driver.current_url == CORVETTE_LINK


def test_optimus_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_OPTIMUS))
    image.click()

    assert driver.current_url == OPTIMUS_LINK


def test_cobra_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_COBRA))
    image.click()

    assert driver.current_url == COBRA_LINK


def test_917kh_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    button = wait.until(EC.element_to_be_clickable(SLIDER_BUTTON_2))
    button.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_917KH))
    image.click()

    assert driver.current_url == POR_917KH_LINK


def test_laferrari_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    button = wait.until(EC.element_to_be_clickable(SLIDER_BUTTON_2))
    button.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_LAFERRARI))
    image.click()

    assert driver.current_url == LAFERRARI_LINK


def test_merc300sl_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    button = wait.until(EC.element_to_be_clickable(SLIDER_BUTTON_2))
    button.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_300SL))
    image.click()

    assert driver.current_url == MERC_300SL_LINK


def test_merc196r_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    button = wait.until(EC.element_to_be_clickable(SLIDER_BUTTON_2))
    button.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_W196R))
    image.click()

    assert driver.current_url == W196R_LINK


def test_etype_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    button = wait.until(EC.element_to_be_clickable(SLIDER_BUTTON_3))
    button.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_ETYPE))
    image.click()

    assert driver.current_url == ETYPE_LINK


def test_firetruck_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    button = wait.until(EC.element_to_be_clickable(SLIDER_BUTTON_3))
    button.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_FIRETRUCK))
    image.click()

    assert driver.current_url == FIRETRUCK_LINK


def test_supersnake_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    button = wait.until(EC.element_to_be_clickable(SLIDER_BUTTON_3))
    button.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_SUPERSNAKE))
    image.click()

    assert driver.current_url == SUPERSNAKE_LINK


def test_leopard_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    button = wait.until(EC.element_to_be_clickable(SLIDER_BUTTON_3))
    button.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_LEOPARD))
    image.click()

    assert driver.current_url == LEOPARD_LINK


def test_007_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    button = wait.until(EC.element_to_be_clickable(SLIDER_BUTTON_4))
    button.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_007))
    image.click()

    assert driver.current_url == LINK_007


def test_gtcollection_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    button = wait.until(EC.element_to_be_clickable(SLIDER_BUTTON_4))
    button.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_GTCOLLECT))
    image.click()

    assert driver.current_url == GTCOLLECT_LINK


def test_box_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    button = wait.until(EC.element_to_be_clickable(SLIDER_BUTTON_4))
    button.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_BOX))
    image.click()

    assert driver.current_url == BOX_LINK


def test_tires_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    all_models = wait.until(EC.element_to_be_clickable(ALL_MODELS))
    all_models.click()

    button = wait.until(EC.element_to_be_clickable(SLIDER_BUTTON_4))
    button.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_TIRES))
    image.click()

    assert driver.current_url == TIRES_LINK