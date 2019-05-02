from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome()
driver.get("http://dev.du-nang.com/admin/dev.html#/login")
print(driver.title)
assert "听果" in driver.title
sleep(2)

managerid=driver.find_element_by_id("inputAdminId")
managerid.send_keys("aaaa")
pwd=driver.find_element_by_id("inputPassword")
pwd.send_keys("bbbb")

elem = driver.find_element_by_class_name("login-btn")
print(elem.text)
elem.click()
sleep(2)
driver.close()