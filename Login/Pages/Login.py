from Login.Locators import *


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element('id', username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('id', password_textbox_id).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element('class name', login_button_classname).click()

    def massage_eror_invalid_login(self):
        self.driver.find_element('xpath', invalid_login_xpath)

    def massage_eror_blank_usernamepassword(self):
        self.driver.find_element('xpath', blank_username_password)
