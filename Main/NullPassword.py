from selenium.webdriver.common.by import By

class NullPassword:

    def __init__(self, driver):
        self.driver = driver
        self.email = "bawdseynat@gmail.com"
        self.email_locator = "/html/body/div/div/div/div/form/div[1]/div/div[1]/div/div/input"
        self.login_button = "/html/body/div/div/div/div/form/button/span/span"

    def NullPassword(self):
        self.driver.find_element_by_xpath(self.email_locator).send_keys(self.email)
        self.driver.find_element_by_xpath(self.login_button).click()
        assert "Please input password" in self.driver.page_source