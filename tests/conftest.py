import pytest
from selenium import webdriver


@pytest.fixture()
def driver_initializer():
	options = webdriver.ChromeOptions()
	options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(options=options)
	driver.maximize_window()
	driver.get("https://demowebshop.tricentis.com/")
	yield driver
	driver.quit()
