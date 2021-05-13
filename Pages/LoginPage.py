from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage



class LoginPage(BasePage):
    GIRIS_YAP_BTTN = (By.CLASS_NAME, "btnSignIn")
    FB_ILE_GIRIS = (By.XPATH, "//*[@class='facebook_large medium facebookBtn  btnLogin']")
    FB_EMAIL = (By.ID,"email")
    FB_PASSWORD = (By.CSS_SELECTOR, "#pass")
    FB_SUBMIT_BTTN = (By.ID, "u_0_0_SS']")



    def __init__(self, driver):
        super().__init__(driver)

    def simple_click(self, by_locator):
        self.driver.find_element(by_locator).click()

    def get_login_page_title(self,title):
        return self.get_title(title)

    def do_login(self,email,password):
        #self.do_click(self.GIRIS_YAP_BTTN)
        #self.do_click(self.FB_ILE_GIRIS)
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        self.do_send_keys(self.FB_EMAIL, email)
        self.do_send_keys(self.FB_PASSWORD, password)
        self.do_click(self.FB_SUBMIT_BTTN)
