import pytest
from POM.login_page import LoginPage


def test_if_user_is_able_to_login(driver_initializer):
	driver = driver_initializer
	l_obj = LoginPage(driver)
	l_obj.login("maire@gmail.com", "marie123")


data = [("John.Doe@gmail.com", "John123"), ("maire@gmail.com", "marie123")]
@pytest.mark.parametrize("username, pwd", data)
def test_if_user_is_logged_in(driver_initializer, username, pwd):
	driver = driver_initializer
	l_obj = LoginPage(driver)
	l_obj.login(username, pwd)
	l_obj.is_user_logged_in()



