import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class CommonFunction:
	version = ""

	@staticmethod
	def set_driver(driver):
		CommonFunction.driver = driver

	@staticmethod
	def set_download_path(path):
		CommonFunction.download_path = path
	   
	#----- web element methods

	def click_element(self, locator, element):
		"""Clicks on a web element specified by locator type and element identifier.
			
        :Args:
         - locator: The type of locator (e.g., By.ID, By.XPATH, By.ITEMID).
		 - element: The locator value of the element to be clicked.
		"""
		self.wait_element(locator, element)
		element_to_click = self.driver.find_element(locator, element)
		element_to_click.click()

		# if locator:
		# 	self.wait_element(locator, element)
		# 	element_to_click = self.driver.find_element(locator, element)
		# 	#ActionChains(self.driver).move_to_element(element_to_click).perform()
		# 	element_to_click.click()

	def type_element(self, locator, element, text, clear=True):
		"""Types text into a web element specified by locator type and element identifier.

		:Args:
         - locator: The type of locator (e.g., By.ID, By.XPATH, By.ITEMID).
		 - element: The locator value of the element to type into.
		 - text: The text to be typed into the element.
		"""
		self.wait_element(locator, element)
		element_to_click = self.driver.find_element(locator, element)
		element_to_click.clear()
		element_to_click.send_keys(text)
		#
		# if locator:
		# 	self.wait_element(locator, element)
		# 	element_to_click = self.driver.find_element(locator, element)
		# 	#ActionChains(self.driver).move_to_element(element_to_click).perform()
		# 	if clear:
		# 		element_to_click.clear()
		# 		element_to_click.send_keys(text)


	def wait_element(self, locator, element, timeout = 60):
		"""Waits for a web element to be clickable or visible.

		:Args:
		 - locator: The type of locator (e.g., By.ID, By.XPATH, By.ITEMID).
		 - element: The locator value of the element to wait for.
		 - timeout: The maximum amount of time to wait (in seconds). Default is 60 seconds.
		"""
		if locator:
			wait = WebDriverWait(self.driver, timeout, poll_frequency=1, ignored_exceptions=[ElementNotInteractableException, TimeoutException])
		try:
			wait.until(EC.element_to_be_clickable((locator, element)))
		except TimeoutException:
			wait.until(EC.visibility_of_element_located((locator, element)))
		except Exception as e:
			print(f"Web element not found: {e}")