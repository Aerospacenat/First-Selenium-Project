from selenium.webdriver.common.by import By

class EmailInvaild:

    def __init__(self, driver):
        self.driver = driver
        self.email = "bawdsey@gmail.com"
        self.password = "Bawdsey123!"
        self.email_locator = "/html/body/div/div/div/div/form/div[1]/div/div[1]/div/div/input"
        self.password_locator = "/html/body/div/div/div/div/form/div[2]/div/div[1]/div/div[1]/div/div[1]/input"
        self.login_button = "/html/body/div/div/div/div/form/button/span/span"

    def EmailInvaild(self):
        self.driver.find_element_by_xpath(self.email_locator).send_keys(self.email)
        self.driver.find_element_by_xpath(self.password_locator).send_keys(self.password)
        self.driver.find_element_by_xpath(self.login_button).click()
        assert isinstance(self.driver.page_source, object)
        assert "Specify license keys" not in self.driver.page_source