from tests.helpers.support_functions import *

statusCode_tab = 'statuscodes-header'
statusCode_content = 'statuscodes-content'

code200 = '//*[@id="200siteAnchor"]'
code305 = '//*[@id="305siteAnchor"]'
code404 = '//*[@id="404siteAnchor"]'
code500 = '//*[@id="500siteAnchor"]'

def click_statusCode_tab(driver_instance):
    elem = driver_instance.find_element_by_id(statusCode_tab)
    elem.click()

def statusCode_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, statusCode_content)
    return elem.is_displayed()

def code200_click(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, code200)
    elem = driver_instance.find_element_by_xpath(code200)
    elem.click()

def code305_click(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, code305)
    elem = driver_instance.find_element_by_xpath(code305)
    elem.click()

def code404_click(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, code404)
    elem = driver_instance.find_element_by_xpath(code404)
    elem.click()

def code500_click(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, code500)
    elem = driver_instance.find_element_by_xpath(code500)
    elem.click()
