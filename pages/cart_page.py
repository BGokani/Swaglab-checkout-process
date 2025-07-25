from Shared.CommonFunction import CommonFunction
from selenium.webdriver.common.by import By
import random

class CartPageLocator:
    btnAddToCart = "shopping_cart_container"
    btnCheckOut = "checkout"
    btnContinue = "continue"
    btnFinish = "finish"
    btnHamburger = "//div[@class='bm-burger-button']"
    btnLogout = "//div[@class='bm-menu']//a[text()='Logout']"

    txtFirstName = "first-name"
    txtLastName = "last-name"
    txtZip = "postal-code"

class CartPage(CommonFunction):

    @staticmethod
    def set_driver(driver):
        CommonFunction.driver = driver

    def select_on_add_to_cart_item(self, item_name):
        for item in item_name:
            self.click_element(By.XPATH, f"//div[text()='{item}']//ancestor::div[@class='inventory_item_description']//following-sibling::div//button[text()='Add to cart']")
            print(f"Add to cart : {item}")

    def select_add_to_cart_item(self):
        self.click_element(By.ID, CartPageLocator.btnAddToCart)

    def get_item_prices(self, item_names):
        prices = []
        for item in item_names:
            try:
                price_element = self.driver.find_element(
                    By.XPATH,f"//div[text()='{item}']//ancestor::div[@class='cart_item_label']//following-sibling::div//div[@class='inventory_item_price']"
                )
                price_text = price_element.text.strip()
                prices.append(price_text)
                print(f"Price of '{item}': {price_text}")
            except Exception as e:
                print(f"Could not get price for {item}: {e}")
                prices.append(None)
        return prices

    def click_on_check_out_btn(self):
        self.click_element(By.ID, CartPageLocator.btnCheckOut)

    def input_for_checkout(self):
        firstName = "TC0" + str(random.randint(1, 99))
        lasName = "TC1" + str(random.randint(1, 99))
        zipCode = "3613" + str(random.randint(1, 99))

        self.type_element(By.ID, CartPageLocator.txtFirstName, firstName)
        self.type_element(By.ID, CartPageLocator.txtLastName, lasName)
        self.type_element(By.ID, CartPageLocator.txtZip, zipCode)

        self.click_element(By.ID, CartPageLocator.btnContinue)

    def get_item_total_price_and_validate(self, expected_prices):
        #itemTotalPrice = self.driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']").text
        taxPrice = self.driver.find_element(By.XPATH, "//div[@class='summary_tax_label']").text
        checkOutPrice = self.driver.find_element(By.XPATH, "//div[@class='summary_total_label']").text

        expectedTotalPrice = 0
        for price in expected_prices:
            expectedTotalPrice += float(price[1:]) # removed last character and add remaining amount. e.g. input: $9 output: 9

        expectedTotalPrice = "$" + str(expectedTotalPrice)

        taxPrice = taxPrice.split(" ")[1]
        expectedCheckoutPrice = float(expectedTotalPrice[1:]) + float(taxPrice[1:])

        expectedCheckoutPrice = "$" + str(expectedCheckoutPrice)
        checkOutPrice = checkOutPrice.split(" ")[1]
        assert (float(checkOutPrice[1:]) == float(expectedCheckoutPrice[1:]),
                "Verify actual and expected checkout price matched : Fail")
        print("Verify actual and expected checkout price matched : Pass")

    def click_on_finish_btn(self):
        self.click_element(By.ID, CartPageLocator.btnFinish)

    def verify_message(self):
        self.driver.find_element(By.XPATH, "//div[@id='checkout_complete_container']")
        print("Msg displayed : Thank you for your order!")

    def click_on_hamburger_and_logout_btn(self):
        """ Clicks the hamburger menu and the logout button.
        """
        self.click_element(By.XPATH, CartPageLocator.btnHamburger)
        self.click_element(By.XPATH, CartPageLocator.btnLogout)




