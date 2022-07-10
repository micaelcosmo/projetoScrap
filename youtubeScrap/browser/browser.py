from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


class NoBrowser:
    def __init__(self):
        self.driver = webdriver.Chrome('.browser/chromedriver.exe')
        self.driver.get("https://www.youtube.com")

    def barra_pesquisa(self):
        self.driver.find_element(By.XPATH, '//*[@id="search-form"]').click()
        self.driver.implicitly_wait(10)
        print('Cliquei!')
        self.driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/'
                                           'form/div[1]/div[1]/div/div[2]/input').send_keys('Pearl Jam')
        self.driver.implicitly_wait(10)
        print('Digitei!')
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/'
                                           'form/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

    def clica_lista(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/'
                                           'ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/'
                                           'div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]').click()
        print('Cliquei no vídeo.')
        sleep(15)
        self.driver.close()


if __name__ == '__main__':
    bb = NoBrowser()
    bb.barra_pesquisa()
    bb.clica_lista()
