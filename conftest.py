import time

import pytest
from selenium import webdriver


def pytest_addoption(parser):
	parser.addoption("--browser_name",
	                 action="store",
	                 default="chrome",
	                 dest="args",
	                 choices=["chrome", "firefox"],
	                 help="sets the browser to execute testcases"
	                 )

	parser.addoption("--env",
	                 choices=["stage", "test"]
	                 )


class TestConfigurations():
	url = "https://demowebshop.tricentis.com/"
	username = "maire@gmail.com"
	password = "marie123"


class StageConfigurations():
	url = "https://demowebshop.tricentis.com/"
	username = "maire1@gmail.com"
	password = "marie123"


@pytest.fixture()
def env_config(request):
	env_ = request.config.option.env

	if env_.lower() == "test":
		return TestConfigurations()
	elif env_.lower() == "stage":
		return StageConfigurations()


@pytest.fixture()
def driver_initializer(request, env_config):
	browser = request.config.option.args

	if browser.lower() == "chrome":
		options = webdriver.ChromeOptions()
		options.add_experimental_option("detach", True)
		driver = webdriver.Chrome(options=options)

	elif browser.lower() == "firefox":
		driver = webdriver.Firefox()

	driver.maximize_window()
	driver.get(env_config.url)
	yield driver
	driver.quit()

