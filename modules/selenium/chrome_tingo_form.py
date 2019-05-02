from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome()
driver.get("http://dev.du-nang.com/admin/dev.html#/login")
print(driver.title)
assert "听果" in driver.title
sleep(2)

print(driver.get_cookies())

managerid=driver.find_element_by_name="adminId"
list =driver.find_elements_by_class_name("load_span")
for m in list:
  print("-----",m.text)
print(managerid)
pwd=driver.find_element_by_id("inputPassword")
pwd.send_keys("123456")
# 截图
driver.get_screenshot_as_file("abc.png")

elem = driver.find_element_by_class_name("login-btn")
print(elem.text)
skip = driver.find_element_by_class_name("skip-btn")

skip.click()
sleep(2)
driver.back()
# elem.click()
sleep(2)
driver.close()