from selenium import webdriver

import time

driver = webdriver.Chrome('/Users/Pao/PycharmProjects/fabrykaTestowPZ/chromedriver.exe')

url = 'https://google.pl'

driver.get(url)

search_box = driver.find_element_by_name('q')

search_box.send_keys('selenium python')

search_box.submit()

time.sleep(5)

driver.quit()

driver.close()
