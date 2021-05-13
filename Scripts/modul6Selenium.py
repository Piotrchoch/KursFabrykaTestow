from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/Piotr/PycharmProjects/taps_git/chromedriver.exe')

driver.get('https://google.pl')

search_box = driver.find_element_by_name('q')
search_box.send_keys('selenium python')
search_box.submit()

time.sleep(5)
driver.quit()
