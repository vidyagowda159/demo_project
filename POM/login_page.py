class LoginPage:

	def __init__(self, driver):
		self.driver = driver

	def login(self):
		self.driver.find_element("link text", "Log in").click()
		self.driver.find_element("id", 'Email').send_keys("John.Doe@gmail.com")
		self.driver.find_element("id", 'Password').send_keys("John123")
		self.driver.find_element("id", 'RememberMe').click()
		self.driver.find_element("class name", 'button-1.login-button').click()








