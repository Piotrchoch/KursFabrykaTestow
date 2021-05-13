from selenium import webdriver
import time


driver = webdriver.Chrome('/Users/Piotr/PycharmProjects/taps_git/chromedriver.exe')

driver.get('https://fabrykatestow.pl')
zakKursy = driver.find_element_by_xpath('/html/body/div[1]/header/div/nav[1]/div/div/div/div[2]/div/div/div/ul/li[2]/a')
zakKursy.click()

kursTAPS = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section/div[2]/div/div/div/div/section[1]/div/div/div[1]/div/div/div/div/div/a')
kursTAPS.click()


elem = driver.find_elements_by_xpath('/html/body/div[1]/main/div/div/div/div/div/div/div/section[5]/div[2]/div/div/div/div/div')
print(elem)
driver.execute_script("arguments[0].scrollIntoView();", elem[0])
driver.save_screenshot("screenshot.png")
time.sleep(5)
driver.quit()
