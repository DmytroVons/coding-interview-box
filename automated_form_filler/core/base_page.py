from time import sleep
from random import uniform
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def click(self, by, value):
        elem = self.driver.find_element(by, value)
        self._human_delay()
        self.actions.move_to_element(elem).click().perform()

    def type(self, by, value, text):
        elem = self.driver.find_element(by, value)
        self._human_delay()
        elem.clear()
        for char in text:
            elem.send_keys(char)
            sleep(uniform(0.05, 0.15))

    def scroll(self, pixels: int):
        self._human_delay()
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def _human_delay(self):
        sleep(uniform(1, 3))
