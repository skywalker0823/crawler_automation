# Introduce selenium
# 1. pip install selenium
# 2. download msedgedriver.exe(For Edge) EX: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# 3. put msedgedriver.exe in same folder of app.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()

driver.get('https://www.google.com.tw/')

element = driver.find_element("name","q")

# Fill in the search box
element.send_keys("Cat")

time.sleep(3)

# Get website element, will get first element matches the condition.
button = driver.find_element("name","btnK")
# If fetch mutiple elements, use find_elements(will make into list)
# buttons = driver.find_elements("name","btnK")

# Therer is a lot of way to get element by
# id, name, class_name, tag_name, link_text, partial_link_text, xpath, css_selector

button.click()

time.sleep(3)
# Or clear the search box
# element.clear()

#  previous page or next page
driver.back()
# driver.forward()

# copy and paste
# element.send_keys(Keys.CONTROL, 'c')
# element.send_keys(Keys.CONTROL, 'v')

# special key bindings : https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys

driver.close()

# If you see the browser open and close, it means success.