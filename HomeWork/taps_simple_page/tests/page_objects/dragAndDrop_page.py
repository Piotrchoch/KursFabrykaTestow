from tests.helpers.support_functions import *

dnd_tab = 'draganddrop-header'
dnd_content = 'draganddrop-content'

def click_dnd_tab(driver_instance):
    elem = driver_instance.find_element_by_id(dnd_tab)
    elem.click()

def dnd_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, dnd_content)
    return elem.is_displayed()
