from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class DataToSheet():
    def __init__(self):
        chrome_driver_path = Service("/Users/israelos/Development/chromedriver")
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)

    def fill_forms(self, addresses_list, prices_list, links_list):
        for i in range(len(addresses_list)):
            self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfUSqEXodLbvKei_wk_9TxLo772ainkPMtqTooLUDF6Uux0Iw"
                            "/viewform?usp=sf_link")
            sleep(2)
            answer = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            answer.send_keys(addresses_list[i], Keys.TAB, prices_list[i], Keys.TAB, links_list[i], Keys.TAB, Keys.ENTER)
