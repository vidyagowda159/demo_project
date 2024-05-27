from POM.login_page import LoginPage


def test_001(driver_initializer):
	driver = driver_initializer
	l_obj = LoginPage(driver)
	l_obj.login()
