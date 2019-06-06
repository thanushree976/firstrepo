from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/dell/Desktop/chromedriver_win32 (3)/Chromedriver.exe")

driver.get("http://www.facebook.com")
driver.find_element_by_name("firstname").send_keys("thanu")
driver.find_element_by_name("lastname").send_keys("shree")
driver.find_element_by_xpath("//input[(@aria-label='Mobile number or email address')]").send_keys("7687654890")
driver.find_element_by_xpath("//input[@value='1']").click()
driver.find_element_by_name("websubmit").click()