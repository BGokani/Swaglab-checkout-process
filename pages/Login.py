import os
import time
from Shared.CommonFunction import CommonFunction
from selenium.webdriver.common.by import By

class LoginLocator:
    txtUserName = "user-name"
    txtPassword = "password"
    btnLogin = "login-button"

class LoginPage(CommonFunction):
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        """ Logs in the user using the provided username and password.
        Args:
            username (str): The username for login.
            password (str): The password for login.
        """
        self.type_element(By.ID, LoginLocator.txtUserName, username)
        self.type_element(By.ID, LoginLocator.txtPassword, password)
        self.click_element(By.ID, LoginLocator.btnLogin)


