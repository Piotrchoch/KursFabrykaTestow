from tests.helpers.support_functions import *
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.switch_to import SwitchTo

form_tab = 'form-header'
form_content = 'form-content'
first_name = '//*[@id="fname"]'
last_name = '//*[@id="lname"]'
submit_button = '//*[@id="formSubmitButton"]'
name = "Piotr"
surname = "Nazwisko"

def click_form_tab(driver_instance):
    elem = driver_instance.find_element_by_id(form_tab)
    elem.click()

def form_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, form_content)
    return elem.is_displayed()

def all_form_filled(driver_instance):
    wait_for_visibility_of_element(driver_instance, last_name, time_to_wait=1)
    firsName = driver_instance.find_element_by_xpath(first_name)
    firsName.send_keys(name)
    secName = driver_instance.find_element_by_xpath(last_name)
    secName.send_keys(surname)
    button = driver_instance.find_element_by_xpath(submit_button)
    button.click()
    MessageText = "success"
    successMessage = Alert(driver_instance)
    if MessageText == successMessage.text:
        return True
    else:
        return False

def only_first_form_filled(driver_instance):
    wait_for_visibility_of_element(driver_instance, last_name, time_to_wait=1)
    firsName = driver_instance.find_element_by_xpath(first_name)
    firsName.send_keys(name)
    button = driver_instance.find_element_by_xpath(submit_button)
    button.click()
    popupMessage = driver_instance.switch_to.active_element.get_attribute("text")
    value = "Wypełnij to pole."
    if value == popupMessage:
        return True
    else:
        return False

def only_second_form_filled(driver_instance):
    wait_for_visibility_of_element(driver_instance, last_name, time_to_wait=1)
    secName = driver_instance.find_element_by_xpath(last_name)
    secName.send_keys(surname)
    button = driver_instance.find_element_by_xpath(submit_button)
    button.click()
    popupMessage = driver_instance.switch_to.active_element.get_attribute("text")
    value = "Wypełnij to pole."
    if value == popupMessage:
        return True
    else:
        return False