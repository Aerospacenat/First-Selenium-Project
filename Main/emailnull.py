from selenium.webdriver.common.by import By

class NullEmail:

    def __init__(self, driver):
        self.driver = driver
        self.password = "Bawdsey123!"
        self.password_locator = "/html/body/div/div/div/div/form/div[2]/div/div[1]/div/div[1]/div/div[1]/input"
        self.login_button = "/html/body/div/div/div/div/form/button/span/span"

    def NullEmail(self):
        self.driver.find_element_by_xpath(self.password_locator).send_keys(self.password)
        self.driver.find_element_by_xpath(self.login_button).click()
        assert "Please input email" in self.driver.page_source