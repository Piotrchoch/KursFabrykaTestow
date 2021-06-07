from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys
from time import sleep

kPress_tab = 'keypresses-header'
kPress_content = 'keypresses-content'
press_field = '//*[@id="target"]'
pressKeyInfo = '//*[@id="keyPressResult"]'

def click_kPress_tab(driver_instance):
    elem = driver_instance.find_element_by_id(kPress_tab)
    elem.click()

def kPress_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, kPress_content)
    return elem.is_displayed()

def kpress_value_info(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, press_field)
    elem = driver_instance.find_element_by_xpath(press_field)
    elem.send_keys(Keys.ENTER)
    sleep(3)
    pressedInfo = driver_instance.find_element_by_xpath(pressKeyInfo)
    if pressedInfo.text == "You entered: ENTER":
        return True
    else:
        return False

