from selenium.webdriver.support import expected_conditions as EC
from locators import MILITARY_MODELS, MODELS, IMAGE_LOTUS_AUTO, IMAGE_007_ASTON_AUTO, IMAGE_CORVETTE_AUTO, IMAGE_OPTIMUS, IMAGE_COBRA_AUTO, IMAGE_917KH_AUTO, IMAGE_LAFERRARI_AUTO, IMAGE_300SL_AUTO, IMAGE_W196R_AUTO, IMAGE_ETYPE_AUTO, IMAGE_FIRETRUCK_AUTO, IMAGE_SUPERSNAKE_AUTO, IMAGE_LEOPARD_MILITARY, LEOPARD_LINK, IMAGE_007, IMAGE_GTCOLLECT_AUTO, IMAGE_BOX, IMAGE_TIRES
from selenium.common.exceptions import ElementNotInteractableException


def test_lotus_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_LOTUS_AUTO).click()
    except ElementNotInteractableException:
        pass


def test_aston007_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_007_ASTON_AUTO).click()
    except ElementNotInteractableException:
        pass


def test_corvette_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_CORVETTE_AUTO).click()
    except ElementNotInteractableException:
        pass


def test_optimus_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_OPTIMUS).click()
    except ElementNotInteractableException:
        pass


def test_cobra_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_COBRA_AUTO).click()
    except ElementNotInteractableException:
        pass


def test_917kh_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_917KH_AUTO).click()
    except ElementNotInteractableException:
        pass


def test_laferrari_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_LAFERRARI_AUTO).click()
    except ElementNotInteractableException:
        pass


def test_merc300sl_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_300SL_AUTO).click()
    except ElementNotInteractableException:
        pass


def test_merc196r_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_W196R_AUTO).click()
    except ElementNotInteractableException:
        pass


def test_etype_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_ETYPE_AUTO).click()
    except ElementNotInteractableException:
        pass


def test_firetruck_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_FIRETRUCK_AUTO).click()
    except ElementNotInteractableException:
        pass


def test_supersnake_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_SUPERSNAKE_AUTO).click()
    except ElementNotInteractableException:
        pass


def test_leopard_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    image = wait.until(EC.element_to_be_clickable(IMAGE_LEOPARD_MILITARY)).click()

    assert driver.current_url == LEOPARD_LINK


def test_007_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_007).click()
    except ElementNotInteractableException:
        pass


def test_gtcollection_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_GTCOLLECT_AUTO).click()
    except ElementNotInteractableException:
        pass


def test_box_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_BOX).click()
    except ElementNotInteractableException:
        pass


def test_tires_website(driver, open_website, wait):

    models = wait.until(EC.element_to_be_clickable(MODELS))
    models.click()

    military_models = wait.until(EC.element_to_be_clickable(MILITARY_MODELS))
    military_models.click()

    try:
        image = driver.find_element(*IMAGE_TIRES).click()
    except ElementNotInteractableException:
        pass

