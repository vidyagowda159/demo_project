
class RegistrationPage:

	def __init__(self, driver):
		self.driver = driver

	def register(self):
		self.driver.find_element("link text", 'Register').click()
		self.driver.find_element("id", "gender-male").click()
		# driver.find_element("id", "gender-female").click()
		self.driver.find_element("id", "FirstName").send_keys("John")
		self.driver.find_element("id", "LastName").send_keys("Doe")
		self.driver.find_element("id", "Email").send_keys("John.Doe@gmail.com")
		self.driver.find_element("id", "Password").send_keys("John123")
		self.driver.find_element("id", "ConfirmPassword").send_keys("John123")
		# driver.find_element("name", "register-button").click()

