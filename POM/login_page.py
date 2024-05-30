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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generic.locators import attach_locators
from generic.excel_lib import read_locators
from generic.wrapper import SeleniumWrapper

loc = read_locators("login_objects")


@attach_locators(loc)       # @wrapper
class LoginPage(SeleniumWrapper):

	def login(self, username, pwd):
		# self.driver.find_element(*self.login_link).click()
		self.click_element(self.login_link)

		# self.driver.find_element(*self.email_txt).send_keys("John.Doe@gmail.com")
		self.enter_text(self.email_txt, value=username)

		# self.driver.find_element(*self.pwd_txt).send_keys("John123")
		self.enter_text(self.pwd_txt, value=pwd)

		# self.driver.find_element(*self.remember_checkbox).click()
		self.click_element(self.remember_checkbox)

		# self.driver.find_element(*self.login_btn).click()
		self.click_element(self.login_btn)

	def is_user_logged_in(self):
		wait_ = WebDriverWait(self.driver, 5)
		webelement = wait_.until(EC.visibility_of_element_located(self.logout_link),
		            message=f"invalid username or password")

		webelement.click()


