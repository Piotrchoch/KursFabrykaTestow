from tests.helpers.support_functions import *

auth_tab = 'basicauth-header'
auth_content = 'basicauth-content'
user_path = '//*[@id="ba_username"]'
password_path = '//*[@id="ba_password"]'
submit_button = '//*[@id="content"]/button'
login_message = '//*[@id="loginFormMessage"]'

def click_authorization_tab(driver_instance):
    elem = driver_instance.find_element_by_id(auth_tab)
    elem.click()

def authorization_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, auth_content)
    return elem.is_displayed()

def tap_all_correct_data(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, password_path)
    username = 'admin'
    password = 'admin'
    user_elem = driver_instance.find_element_by_xpath(user_path)
    user_elem.send_keys(username)
    password_elem = driver_instance.find_element_by_xpath(password_path)
    password_elem.send_keys(password)
    button = driver_instance.find_element_by_xpath(submit_button)
    button.click()

def tap_usernme_incorrect_data(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, password_path)
    username = 'admin1'
    password = 'admin'
    user_elem = driver_instance.find_element_by_xpath(user_path)
    user_elem.send_keys(username)
    password_elem = driver_instance.find_element_by_xpath(password_path)
    password_elem.send_keys(password)
    button = driver_instance.find_element_by_xpath(submit_button)
    button.click()
    wait_for_visibility_of_element_by_xpath(driver_instance, login_message)
    invalid = driver_instance.find_element_by_xpath(login_message)
    if invalid.is_displayed():
        return True
    else:
        return False

def tap_password_incorrect_data(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, password_path)
    username = 'admin'
    password = 'admin1'
    user_elem = driver_instance.find_element_by_xpath(user_path)
    user_elem.send_keys(username)
    password_elem = driver_instance.find_element_by_xpath(password_path)
    password_elem.send_keys(password)
    button = driver_instance.find_element_by_xpath(submit_button)
    button.click()
    wait_for_visibility_of_element_by_xpath(driver_instance, login_message)
    invalid = driver_instance.find_element_by_xpath(login_message)
    if invalid.is_displayed():
        return True
    else:
        return False