from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://simpletestsite.fabrykatestow.pl/")
myDynamicElement = driver.find_element_by_id("checkbox-header")
driver.quit()
