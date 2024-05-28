# class LoginPage:
# 	login_link = "link text", "Log in"
# 	email_txt = "id", 'Email'
# 	pwd_txt = "id", 'Password'
# 	remember_checkbox = "id", 'RememberMe'
# 	login_btn = "class name", 'button-1.login-button'
#
# 	def __init__(self, driver):
# 		self.driver = driver
#
# 	def login(self):
# 		self.driver.find_element(*self.login_link).click()
# 		self.driver.find_element(*self.email_txt).send_keys("John.Doe@gmail.com")
# 		self.driver.find_element(*self.pwd_txt).send_keys("John123")
# 		self.driver.find_element(*self.remember_checkbox).click()
# 		# self.driver.find_element(*self.login_btn).click()

################################################################################
# maintaining locators in external file
# from generic.excel_lib import read_locators
#
#
# class LoginPage:
# 	locators = read_locators("login_objects")
#
# 	def __init__(self, driver):
# 		self.driver = driver
#
# 	def login(self):
# 		self.driver.find_element(*self.locators["login_link"]).click()
# 		self.driver.find_element(*self.locators["email_txt"]).send_keys("John.Doe@gmail.com")
# 		self.driver.find_element(*self.locators["pwd_txt"]).send_keys("John123")
# 		self.driver.find_element(*self.locators["remember_checkbox"]).click()
# 		self.driver.find_element(*self.locators["login_btn"]).click()

#################################################################################
from generic.locators import attach_locators
from generic.excel_lib import read_locators

loc = read_locators("login_objects")

@attach_locators(loc)
class LoginPage:
	def __init__(self, driver):
		self.driver = driver

	def login(self):
		self.driver.find_element(*self.login_link).click()
		self.driver.find_element(*self.email_txt).send_keys("John.Doe@gmail.com")
		self.driver.find_element(*self.pwd_txt).send_keys("John123")
		self.driver.find_element(*self.remember_checkbox).click()
		# self.driver.find_element(*self.login_btn).click()
