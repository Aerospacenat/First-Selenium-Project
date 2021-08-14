from selenium.webdriver.common.by import By

class NullInput:

    def __init__(self, driver):
        self.driver = driver
        self.login_button = "/html/body/div/div/div/div/form/button/span/span"

    def NullInput(self):
        self.driver.find_element_by_xpath(self.login_button).click()
        assert "Please input email" in self.driver.page_source
        assert "Please input password" in self.driver.page_source