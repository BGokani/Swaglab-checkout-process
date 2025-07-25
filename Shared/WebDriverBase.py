import os
import unittest
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from Shared.CommonFunction import CommonFunction
from selenium.webdriver.chrome.options import Options
from pages.cart_page import CartPage


class WebDriverBase(unittest.TestCase):
    driver: webdriver.Chrome = None

    @classmethod
    def setUpClass(cls):
        """Initialize WebDriver once per test class."""
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option("useAutomationExtension", False)
            chrome_options.add_experimental_option("prefs", {"credentials_enable_service": False,
                "profile.password_manager_enabled": False
            })
            #driver = webdriver.Chrome(options=chrome_options)
            options = webdriver.ChromeOptions()

            cls.driver = webdriver.Chrome(options=options)
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)

            # Register the driver with CommanFunctions utility
            CommonFunction.set_driver(cls.driver)
            CartPage.set_driver(cls.driver)

        except WebDriverException as e:
            raise RuntimeError(f"Failed to start WebDriver: {e}")

    @classmethod
    def tearDownClass(cls):
        """ Quit WebDriver once after all tests in the class."""
        if cls.driver:
            cls.driver.quit()

    def save_screenshot(self, name: str = None):
        name = name or self._testMethodName
        path = os.path.join(
            os.getcwd(), "screenshots", f"{name}_{datetime.now():%Y%m%d_%H%M%S}.png"
        )
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.driver.save_screenshot(path)
