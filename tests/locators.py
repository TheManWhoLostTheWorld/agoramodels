from selenium.webdriver.common.by import By

# Social Network Links
TWITTER_BUTTON_HEADER = (By.XPATH, '//div[@class="col-6 col-sm-6"]/ul/li[1]')
FACEBOOK_BUTTON_HEADER = (By.XPATH, '//div[@class="col-6 col-sm-6"]/ul/li[2]/a')
YOUTUBE_BUTTON_HEADER = (By.XPATH, '//div[@class="col-6 col-sm-6"]/ul/li[3]/a')
YOUTUBE_ACCEPT_BUTTON = (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span')
INSTAGRAM_BUTTON_HEADER = (By.XPATH, '//div[@class="col-6 col-sm-6"]/ul/li[4]/a')
TWITTER_BUTTON_FOOTER = (By.XPATH, '//div[@id="footer"]/footer/div/div/div[2]/li[1]/a')
FACEBOOK_BUTTON_FOOTER = (By.XPATH, '//div[@id="footer"]/footer/div/div/div[2]/li[2]/a/i')
YOUTUBE_BUTTON_FOOTER = (By.XPATH, '//div[@id="footer"]/footer/div/div/div[2]/li[3]/a/i')
INSTAGRAM_BUTTON_FOOTER = (By.XPATH, '//div[@id="footer"]/footer/div/div/div[2]/li[4]/a/i')
TWITTER_LOAD = (By.XPATH, "//div[@class='css-175oi2r r-1awozwy']")
FACEBOOK_LOAD = (By.XPATH, '//div[@role="banner"]')
YOUTUBE_LOAD = (By.XPATH, "//a[@id='logo']")
INSTAGRAM_LOAD = (By.XPATH, "//div[@class='_aagx']")

# Social Networks Websites
MAIN_PAGE = "https://www.agoramodels.com/de/"
TWITTER_PAGE = "https://twitter.com/AgoraModels"
FACEBOOK_PAGE = "https://www.facebook.com/AgoraModelsDE"
YOUTUBE_PAGE = "https://www.youtube.com/AgoraModels"
INSTAGRAM_PAGE = "https://www.instagram.com/agoramodels/"

# Main Menu Locators
MODEL_TALK_PAGE = "https://www.agoramodels.com/de/model-talk/"
EXPERTS_PAGE = "https://www.agoramodels.com/de/experts/"
DOWNLOAD_PAGE = "https://www.agoramodels.com/de/download-center/"
MY_ACCOUNT_PAGE = "https://www.agoramodels.com/de/portal-sso/"
FORUM_PAGE = "https://community.agoramodels.com/"
SUPPORT_PAGE = "https://support.agoramodels.com/hc/de"

# Main Menu Pages
MAIN_PAGE_BUTTON = (By.XPATH, "//a[contains(text(),'Startseite')]")
MODEL_TALK_BUTTON = (By.XPATH, "//a[contains(text(),'Model-Talk')]")
EXPERTS_BUTTON = (By.XPATH, "//a[contains(text(),'Expertenverzeichnis')]")
DOWNLOAD_BUTTON = (By.XPATH, "//a[contains(text(),'Download-Center')]")
MY_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(text(),'Mein Könto')]")
FORUM_BUTTON = (By.XPATH, "//a[contains(text(),'Modellbauforum')]")
SUPPORT_BUTTON = (By.XPATH, "//a[contains(text(),'Unterstützung')]")

# Types of models
ALL_MODELS = (By.XPATH, "//a[contains(text(),'Alle')]")
CARS_MODELS = (By.XPATH, "//a[contains(text(),'Fahrzeuge')]")
MILITARY_MODELS = (By.XPATH, "//a[contains(text(),'Militärisch')]")
MODELS_007 = (By.XPATH, "//a[contains(text(),'007')]")
IMAGE_LOTUS = "https://www.agoramodels.com/site/assets/files/15177/ger.174x0.png"
IMAGE_007_ASTON = "	https://www.agoramodels.com/site/assets/files/14603/ger-1.174x0.png"
IMAGE_CORVETTE = "https://www.agoramodels.com/site/assets/files/14605/ger.174x0.png"
IMAGE_COBRA = "https://www.agoramodels.com/site/assets/files/14607/ger.174x0.png"
IMAGE_LAFERRARI = "https://www.agoramodels.com/site/assets/files/14604/ger.174x0.jpg"
IMAGE_300SL = "https://www.agoramodels.com/site/assets/files/14608/mercedes_300_german.174x0.jpg"
IMAGE_W196R = "https://www.agoramodels.com/site/assets/files/14609/ger.174x0.png"
IMAGE_ETYPE = "https://www.agoramodels.com/site/assets/files/14610/jaguar_german.174x0.jpg"
IMAGE_917KH = "https://www.agoramodels.com/site/assets/files/14612/ger.174x0.png"
IMAGE_FIRETRUCK = "https://www.agoramodels.com/site/assets/files/14613/fdny_german.174x0.jpg"
IMAGE_SUPERSNAKE = "https://www.agoramodels.com/site/assets/files/14614/super_snake_german.174x0.jpg"
IMAGE_GTCOLLECT = "https://www.agoramodels.com/site/assets/files/14624/ferrari_gt.174x0.jpg"
IMAGE_OPTIMUS = "https://www.agoramodels.com/site/assets/files/14606/optimus_prime_78cm.174x0.png"
IMAGE_LEOPARD = "https://www.agoramodels.com/site/assets/files/14615/leopard_german.174x0.jpg"
IMAGE_007 = "https://www.agoramodels.com/site/assets/files/14617/007.174x0.jpg"
IMAGE_BOX = "https://www.agoramodels.com/site/assets/files/14625/case_1.174x0.jpg"
IMAGE_TIRES = "https://www.agoramodels.com/site/assets/files/15414/wheel_stack.174x0.jpg"