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
MODELS = (By.XPATH, "//a[contains(text(),'Modelle')]")

# Types of models (all)
ALL_MODELS = (By.XPATH, "//a[contains(text(),'Alle')]")
CARS_MODELS = (By.XPATH, "//a[contains(text(),'Fahrzeuge')]")
MILITARY_MODELS = (By.XPATH, "//a[contains(text(),'Militärisch')]")
MODELS_007 = (By.XPATH, "//a[contains(text(),'007')]")
LOTUS_LINK = "https://www.agoramodels.com/de/wet-nellie/"
ASTON_007_LINK = "https://www.agoramodels.com/de/007_db5/"
CORVETTE_LINK = "https://www.agoramodels.com/de/1963-corvette-sting-ray/"
COBRA_LINK = "https://www.agoramodels.com/de/shelby-cobra/"
LAFERRARI_LINK = "https://www.agoramodels.com/de/laferrari/"
MERC_300SL_LINK = "https://www.agoramodels.com/de/mercedes300sl/"
W196R_LINK = "https://www.agoramodels.com/de/1955-mercedes-w196/"
ETYPE_LINK = "https://www.agoramodels.com/de/jaguar/"
POR_917KH_LINK = "https://www.agoramodels.com/de/porsche-917/"
FIRETRUCK_LINK = "https://www.agoramodels.com/de/fdny/"
SUPERSNAKE_LINK = "https://www.agoramodels.com/de/1967-shelby-mustang-super-snake/"
GTCOLLECT_LINK = "https://www.agoramodels.com/de/ferrarigt-1/"
OPTIMUS_LINK = "https://www.agoramodels.com/de/optimus-prime/"
LEOPARD_LINK = "https://www.agoramodels.com/de/leopard/"
LINK_007 = "https://www.agoramodels.com/de/007/"
BOX_LINK = "https://www.agoramodels.com/de/display-cases/"
TIRES_LINK = "https://www.agoramodels.com/de/speedway-tires/"
LIST_OF_ALL_MODELS = ["Esprit - Der Spion, der mich liebte", "DB5 - Keine Zeit zu sterben", "1963 Corvette Sting Ray", "Optimus Prime", "1965 Shelby Cobra 427 SC", "Porsche 917KH", "LaFerrari", "Mercedes 300SL Gullwing", "Mercedes W196R", "Jaguar E-Type", "FDNY Fire Truck", "1967 Shelby Mustang Super Snake", "Leopard 2A6", "007", "Ferrari GT-Kollektion", "Vitrinen", "Shelby Mustang Wheel Set"]
IMAGE_LOTUS = (By.XPATH, "(//img[@src='/site/assets/files/15177/ger.174x0.png'])[1]")
IMAGE_007_ASTON = (By.XPATH, "(//img[@src='/site/assets/files/14603/ger-1.174x0.png'])[1]")
IMAGE_CORVETTE = (By.XPATH, "(//img[@src='/site/assets/files/14605/ger.174x0.png'])[1]")
IMAGE_COBRA = (By.XPATH, "(//img[@src='/site/assets/files/14607/ger.174x0.png'])[1]")
IMAGE_LAFERRARI = (By.XPATH, "(//img[@src='/site/assets/files/14604/ger.174x0.jpg'])[1]")
IMAGE_300SL = (By.XPATH, "(//img[@src='/site/assets/files/14608/mercedes_300_german.174x0.jpg'])[1]")
IMAGE_W196R = (By.XPATH, "(//img[@src='/site/assets/files/14609/ger.174x0.png'])[1]")
IMAGE_ETYPE = (By.XPATH, "(//img[@src='/site/assets/files/14610/jaguar_german.174x0.jpg'])[1]")
IMAGE_917KH = (By.XPATH, "(//img[@src='/site/assets/files/14612/ger.174x0.png'])[1]")
IMAGE_FIRETRUCK = (By.XPATH, "(//img[@src='/site/assets/files/14613/fdny_german.174x0.jpg'])[1]")
IMAGE_SUPERSNAKE = (By.XPATH, "(//img[@src='/site/assets/files/14614/super_snake_german.174x0.jpg'])[1]")
IMAGE_GTCOLLECT = (By.XPATH, "(//img[@src='/site/assets/files/14624/ferrari_gt.174x0.jpg'])[1]")
IMAGE_OPTIMUS = (By.XPATH, "(//img[@src='/site/assets/files/14606/optimus_prime_78cm.174x0.png'])[1]")
IMAGE_LEOPARD = (By.XPATH, "(//img[@src='/site/assets/files/14615/leopard_german.174x0.jpg'])[1]")
IMAGE_007 = (By.XPATH, "(//img[@src='/site/assets/files/14617/007.174x0.jpg'])[1]")
IMAGE_BOX = (By.XPATH, "(//img[@src='/site/assets/files/14625/case_1.174x0.jpg'])[1]")
IMAGE_TIRES = (By.XPATH, "(//img[@src='/site/assets/files/15414/wheel_stack.174x0.jpg'])[1]")

# Types of models (auto)
IMAGE_LOTUS_AUTO = (By.XPATH, "(//img[@src='/site/assets/files/15177/ger.174x0.png'])[2]")
IMAGE_007_ASTON_AUTO = (By.XPATH, "(//img[@src='/site/assets/files/14603/ger-1.174x0.png'])[2]")
IMAGE_CORVETTE_AUTO = (By.XPATH, "(//img[@src='/site/assets/files/14605/ger.174x0.png'])[2]")
IMAGE_COBRA_AUTO = (By.XPATH, "(//img[@src='/site/assets/files/14607/ger.174x0.png'])[2]")
IMAGE_LAFERRARI_AUTO = (By.XPATH, "(//img[@src='/site/assets/files/14604/ger.174x0.jpg'])[2]")
IMAGE_300SL_AUTO = (By.XPATH, "(//img[@src='/site/assets/files/14608/mercedes_300_german.174x0.jpg'])[2]")
IMAGE_W196R_AUTO = (By.XPATH, "(//img[@src='/site/assets/files/14609/ger.174x0.png'])[2]")
IMAGE_ETYPE_AUTO = (By.XPATH, "(//img[@src='/site/assets/files/14610/jaguar_german.174x0.jpg'])[2]")
IMAGE_917KH_AUTO = (By.XPATH, "(//img[@src='/site/assets/files/14612/ger.174x0.png'])[2]")
IMAGE_FIRETRUCK_AUTO = (By.XPATH, "(//img[@src='/site/assets/files/14613/fdny_german.174x0.jpg'])[2]")
IMAGE_SUPERSNAKE_AUTO = (By.XPATH, "(//img[@src='/site/assets/files/14614/super_snake_german.174x0.jpg'])[2]")
IMAGE_GTCOLLECT_AUTO = (By.XPATH, "(//img[@src='/site/assets/files/14624/ferrari_gt.174x0.jpg'])[2]")

# Types of models military
IMAGE_LEOPARD_MILITARY = (By.XPATH, "(//img[@src='/site/assets/files/14615/leopard_german.174x0.jpg'])[2]")

# Types of models 007
IMAGE_007_007 = (By.XPATH, "(//img[@src='/site/assets/files/14617/007.174x0.jpg'])[3]")
IMAGE_LOTUS_007 = (By.XPATH, "(//img[@src='/site/assets/files/15177/ger.174x0.png'])[3]")
IMAGE_007_ASTON_007 = (By.XPATH, "(//img[@src='/site/assets/files/14603/ger-1.174x0.png'])[3]")

SLIDER_BUTTON_2 = (By.XPATH, "(//button[@class='owl-dot'])[1]")
SLIDER_BUTTON_3 = (By.XPATH, "(//button[@class='owl-dot'])[2]")
SLIDER_BUTTON_4 = (By.XPATH, "(//button[@class='owl-dot'])[3]")