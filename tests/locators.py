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

# Website
MAIN_PAGE = "https://www.agoramodels.com/"
TWITTER_PAGE = "https://twitter.com/AgoraModels"
FACEBOOK_PAGE = "https://www.facebook.com/AgoraModelsDE"
YOUTUBE_PAGE = "https://www.youtube.com/AgoraModels"
INSTAGRAM_PAGE = "https://www.instagram.com/agoramodels/"