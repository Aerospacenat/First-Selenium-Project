from selenium import webdriver
from loginpage import *
from emailnull import *
from NullPassword import *
from Nullinput import *
from InvalidEmail import *
from logout import *

def setup():
    return webdriver.Chrome(executable_path=r"C:\Users\natty\PycharmProjects\SeleniumTest\chromedriver.exe")

def logintest():
    driver = setup()
    driver.get("https://account.acronis.com/#/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    login_form = Login(driver)
    login_form.login()
    print("Test 1 Complete")
    driver.quit()

def emailNegtest():
    driver = setup()
    driver.get("https://account.acronis.com/#/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    email_null = NullEmail(driver)
    email_null.NullEmail()
    print("Test 2 Complete")
    driver.quit()

def passwordNegtest():
    driver = setup()
    driver.get("https://account.acronis.com/#/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    pass_null = NullPassword(driver)
    pass_null.NullPassword()
    print("Test 3 Complete")
    driver.quit()

def nullinputtest():
    driver = setup()
    driver.get("https://account.acronis.com/#/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    input_null = NullInput(driver)
    input_null.NullInput()
    print("Test 4 Complete")
    driver.quit()

def invalidEmailtest():
    driver = setup()
    driver.get("https://account.acronis.com/#/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    invaild_email = EmailInvaild(driver)
    invaild_email.EmailInvaild()
    print("Test 5 Complete")
    driver.quit()

def logouttest():
    driver = setup()
    driver.get("https://account.acronis.com/#/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    login_form = Login(driver)
    login_form.login()
    logout_form = Logout(driver)
    logout_form.logout()
    print("Test 6 Complete")
    driver.quit()

if __name__ == "__main__":
    logintest()
    emailNegtest()
    passwordNegtest()
    nullinputtest()
    invalidEmailtest()
    logouttest()