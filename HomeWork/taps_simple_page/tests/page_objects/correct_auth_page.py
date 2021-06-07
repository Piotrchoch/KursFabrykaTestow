from tests.helpers.support_functions import *

loggedIn = 'loggedInMessage'


def correct_auth(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, loggedIn)
    return elem.is_displayed()
