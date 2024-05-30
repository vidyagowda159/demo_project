from datetime import datetime
import pytest
from POM.login_page import LoginPage

# pytestmark = pytest.mark.usefixtures("driver_initializer")

def test_if_user_is_able_to_login(driver_initializer, env_config):
	driver = driver_initializer
	l_obj = LoginPage(driver)
	l_obj.login(env_config.username, env_config.password)
	dt = datetime.now()
	date = f'{dt.year}-{dt.day}-{dt.month}'
	time_ = f"{dt.hour}-{dt.minute}-{dt.second}"

	driver.save_screenshot(f"login_page{date}-{time_}.png")
	l_obj.is_user_logged_in()


# data = [("maire@gmail.com", "marie123"), ("John.Doe@gmail.com", "John123")]
# @pytest.mark.parametrize("username, pwd", data)
# def test_if_user_is_logged_in(driver_initializer, username, pwd):
# 	driver = driver_initializer
# 	l_obj = LoginPage(driver)
# 	l_obj.login(username, pwd)
# 	l_obj.is_user_logged_in()



