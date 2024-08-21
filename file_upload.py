# autoit, pyautogui
import time
import pyautogui
from selenium import webdriver

c_options = webdriver.ChromeOptions()
c_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=c_options)

driver.get("https://www.freepdfconvert.com/")

driver.find_element("xpath", '//a[@class="btn-wrapper upload-btn"]').click()

path = r"C:\Users\Vidyashree M C\demo_project\requirements.txt"

time.sleep(3)
pyautogui.write(path)
pyautogui.press("enter")

