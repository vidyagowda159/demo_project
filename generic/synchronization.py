from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException


def _wait(func):        # func -> click_element
	def wrapper(*args, **kwargs):   # args -> (self, locator)
		instance_dict, locator = args
		wait_ = WebDriverWait(instance_dict.driver, 10)
		element = wait_.until(EC.visibility_of_element_located(locator),
		                      message=f"{locator} is not visible")

		if element.is_enabled():
			return func(*args, **kwargs)
		raise ElementNotInteractableException(f"{locator} is not interactable")

	return wrapper