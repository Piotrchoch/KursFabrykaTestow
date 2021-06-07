from tests.helpers.support_functions import *

iFrame_tab = 'iframe-header'
iFrame_content = 'iframe-content'
button1 = 'simpleButton1'
button2 = 'simpleButton2'
message = 'whichButtonIsClickedMessage'

def click_iFrame_tab(driver_instance):
    elem = driver_instance.find_element_by_id(iFrame_tab)
    elem.click()

def iFrame_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, iFrame_content)
    return elem.is_displayed()

def button1_clicked(driver_instance):
    driver_instance.switch_to.frame(0)
    wait_for_visibility_of_element(driver_instance, button1)
    but1 = driver_instance.find_element_by_id(button1)
    but1.click()
    wait_for_visibility_of_element(driver_instance, message)
    buttonInfo = driver_instance.find_element_by_id(message)
    if buttonInfo == "Button 1 was clicked!":
        return True
    else:
        return False

def button2_clicked(driver_instance):
    driver_instance.switch_to.frame(0)
    wait_for_visibility_of_element(driver_instance, button2)
    but2 = driver_instance.find_element_by_id(button2)
    but2.click()
    wait_for_visibility_of_element(driver_instance, message)
    buttonInfo = driver_instance.find_element_by_id(message)
    if buttonInfo == "Button 2 was clicked!":
        return True
    else:
        return False

