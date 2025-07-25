import unittest
from selenium.webdriver.common.by import By

from Shared.WebDriverBase import WebDriverBase
from config.config import LoginTestData
from Shared.CommonFunction import CommonFunction
from pages.Login import LoginPage, LoginLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage


class LoginTest(WebDriverBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.cf = CommonFunction()
        cls.login_page = LoginPage(cls.driver)
        cls.cart_page = CartPage()
        cls.driver.get(LoginTestData.url)

    def setUp(self):
        """Navigate to login page before every test to reset state."""
        self.driver.get(LoginTestData.url)

    def test_AA_verify_complete_purchase_flow(self):
        """R_TC: Verify End-to-end validation of the full purchase flow """
        try:
            item_names = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

            self.login_page.login(LoginTestData.username, LoginTestData.password)

            element = self.driver.find_element(By.XPATH,"//span[text()='Products']")
            assert element.is_displayed(), "Verify user login successfully : Fail"
            print("Verify user login successfully : Pass")

            self.cart_page.select_on_add_to_cart_item(item_names)
            self.cart_page.select_add_to_cart_item()
            print("Successfully Added Items")

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
            )

            # Extract items
            cart_elements = self.driver.find_elements(By.XPATH, "//div[@class='cart_item']")
            actual_items = []
            actual_prices = []

            for item in cart_elements:
                try:
                    name = item.find_element(By.XPATH, ".//div[@class='inventory_item_name']").text
                    price = item.find_element(By.XPATH, ".//div[@class='inventory_item_price']").text
                    actual_items.append(name.strip())
                    actual_prices.append(price.strip())

                except Exception as e:
                    print(f"Skipping item due to error: {e}")

            self.assertEqual(actual_items, item_names, "All Value is match : Fail")
            print("All Value is match : Pass")

            expected_prices = self.cart_page.get_item_prices(item_names)

            self.assertEqual(actual_prices, expected_prices, "Item prices do not match : Fail")
            print("Item prices match: Pass")

            self.cart_page.click_on_check_out_btn()
            self.cart_page.input_for_checkout()
            self.cart_page.get_item_total_price_and_validate(expected_prices)
            self.cart_page.click_on_finish_btn()
            self.cart_page.verify_message()
            self.cart_page.click_on_hamburger_and_logout_btn()

            element = self.driver.find_element(By.ID, "login-button")
            assert element.is_displayed(), "Verify user logout : Fail"
            print("Verify user logout : Pass")

        except Exception as e:
            self.save_screenshot("login_failure")
            print(f"Test failed: {e}")
            raise

if __name__ == "__main__":
    unittest.main()
