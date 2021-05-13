from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class Homepage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)