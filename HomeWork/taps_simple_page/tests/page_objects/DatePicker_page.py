from tests.helpers.support_functions import *

date_tab = 'datepicker-header'
date_content = 'datepicker-content'
date_input = '//*[@id="start"]'

def click_date_tab(driver_instance):
    elem = driver_instance.find_element_by_id(date_tab)
    elem.click()

def date_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, date_content)
    return elem.is_displayed()

def  choose_correct_date(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, date_input)
    elem = driver_instance.find_element_by_xpath(date_input)
    correct_date = "2020-06-18"
    elem.send_keys(correct_date)
    chosen_date = elem.get_attribute("value")
    if chosen_date == correct_date:
        return True
    else:
        return False

def choose_incorrect_LessThanMin_date(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, date_input)
    elem = driver_instance.find_element_by_xpath(date_input)
    correct_date = '2019-12-31'
    elem.send_keys(correct_date)
    chosen_date = elem.get_attribute("value")
    if chosen_date == correct_date:
        return False
    else:
        return True

def choose_incorrect_MoreThanMax_date(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, date_input)
    elem = driver_instance.find_element_by_xpath(date_input)
    correct_date = '2021-01-01'
    elem.send_keys(correct_date)
    chosen_date = elem.get_attribute("value")
    if chosen_date == correct_date:
        return False
    else:
        return True