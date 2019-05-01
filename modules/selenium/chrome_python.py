from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome()
driver.get("http://www.python.org")
# driver.get("http://www.baidu.com")
print(driver.title)
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
sleep(5)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
sleep(5)
# driver.close()