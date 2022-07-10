from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


class NoBrowser:
    def __init__(self):
        driver = webdriver.Chrome('./chromedriver')
        driver.get("https://www.youtube.com")
        
