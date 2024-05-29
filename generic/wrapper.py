from generic.synchronization import _wait


class SeleniumWrapper:
	""" generic utilities for selenium webdriver actions"""

	def __init__(self, driver):
		self.driver = driver

	@_wait                  # click_element = _wait(click_element)
	def click_element(self, locator):
		self.driver.find_element(*locator).click()

	@_wait
	def enter_text(self, locator, *, value):
		self.driver.find_element(*locator).send_keys(value)


