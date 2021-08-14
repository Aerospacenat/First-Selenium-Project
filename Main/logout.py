from selenium.webdriver.common.by import By

class Logout:

    def __init__(self, driver):
        self.driver = driver
        self.profile_locator = "/html/body/div/section/section/header/div[2]/div/div/button/span"
        self.accept_locator = "onetrust-accept-btn-handler"
        self.logout_locator = "/html/body/div[2]/div/div/ul/li[4]"
        self.login_button = "/html/body/div/div/div/div/form/button/span/span"


    def logout(self):
        self.driver.find_element_by_xpath(self.profile_locator).click()
        #print(self.driver.find_element_by_xpath(self.logout_locator))
        self.driver.find_element_by_xpath(self.logout_locator).click()
        assert "Account" in self.driver.page_source
