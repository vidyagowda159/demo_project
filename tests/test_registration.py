from POM.register_page import RegistrationPage


def test_001(driver_initializer):
	"""validates if user is able to register"""
	driver = driver_initializer
	r_obj = RegistrationPage(driver)
	r_obj.register()
