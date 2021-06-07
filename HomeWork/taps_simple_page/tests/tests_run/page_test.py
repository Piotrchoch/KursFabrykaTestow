import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, checkboxes_page, hovers_page, users_page, inputs_page, dropdown_page, add_remove_page, DatePicker_page, auth_page, correct_auth_page, form_page, key_press_page, iFrame_page, statusCode_page, statusCode_clicked_page, dragAndDrop_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_input_visibility(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test5_input_correct_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_keys_to_input(self.driver))

    def test6_input_incorrect_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test8_add_new_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_elem(self.driver)

    def test9_remove_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_elem(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))


    #testowanie elementów zadanie domowe

    #data picker
    def test10_choose_correct_date(self):
        DatePicker_page.click_date_tab(self.driver)
        self.assertTrue(DatePicker_page.date_content_visible(self.driver))
        DatePicker_page.choose_correct_date(self.driver)

    def test11_choose_incorrect_lessmin_date(self):
        DatePicker_page.click_date_tab(self.driver)
        self.assertTrue(DatePicker_page.date_content_visible(self.driver))
        DatePicker_page.choose_incorrect_LessThanMin_date(self.driver)

    def test12_choose_incorrect_moremax_date(self):
        DatePicker_page.click_date_tab(self.driver)
        self.assertTrue(DatePicker_page.date_content_visible(self.driver))
        DatePicker_page.choose_incorrect_MoreThanMax_date(self.driver)


    #basic auth
    def test13_correct_auth(self):
        auth_page.click_authorization_tab(self.driver)
        self.assertTrue(auth_page.authorization_content_visible(self.driver))
        auth_page.tap_all_correct_data(self.driver)
        self.assertTrue(correct_auth_page.correct_auth(self.driver))

    def test14_auth_incorrect_username(self):
        auth_page.click_authorization_tab(self.driver)
        self.assertTrue(auth_page.authorization_content_visible(self.driver))
        auth_page.tap_usernme_incorrect_data(self.driver)

    def test15_auth_incorrect_password(self):
        auth_page.click_authorization_tab(self.driver)
        self.assertTrue(auth_page.authorization_content_visible(self.driver))
        auth_page.tap_password_incorrect_data(self.driver)


    #form
    def test16_all_forms_filled(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))
        form_page.all_form_filled(self.driver)

    def test17_only_first_form_filled(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))
        form_page.only_first_form_filled(self.driver)

    def test18_only_second_form_filled(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))
        form_page.only_second_form_filled(self.driver)


    #key press
    def test19_key_press(self):
        key_press_page.click_kPress_tab(self.driver)
        self.assertTrue(key_press_page.kPress_content_visible(self.driver))
        key_press_page.kpress_value_info(self.driver)


    #iFrames
    def test20_iFrames_info_button1(self):
        iFrame_page.click_iFrame_tab(self.driver)
        self.assertTrue(iFrame_page.iFrame_content_visible(self.driver))
        iFrame_page.button1_clicked(self.driver)

    def test21_iFrames_info_button2(self):
        iFrame_page.click_iFrame_tab(self.driver)
        self.assertTrue(iFrame_page.iFrame_content_visible(self.driver))
        iFrame_page.button2_clicked(self.driver)

    #status code
    def test22_statusCode_200(self):
        statusCode_page.click_statusCode_tab(self.driver)
        self.assertTrue(statusCode_page.statusCode_content_visible(self.driver))
        statusCode_page.code200_click(self.driver)
        self.assertTrue(statusCode_clicked_page.statusCode_200(self.driver))

    def test23_statusCode_305(self):
        statusCode_page.click_statusCode_tab(self.driver)
        self.assertTrue(statusCode_page.statusCode_content_visible(self.driver))
        statusCode_page.code305_click(self.driver)
        self.assertTrue(statusCode_clicked_page.statusCode_305(self.driver))

    def test24_statusCode_404(self):
        statusCode_page.click_statusCode_tab(self.driver)
        self.assertTrue(statusCode_page.statusCode_content_visible(self.driver))
        statusCode_page.code404_click(self.driver)
        self.assertTrue(statusCode_clicked_page.statusCode_404(self.driver))

    def test25_statusCode_500(self):
        statusCode_page.click_statusCode_tab(self.driver)
        self.assertTrue(statusCode_page.statusCode_content_visible(self.driver))
        statusCode_page.code500_click(self.driver)
        self.assertTrue(statusCode_clicked_page.statusCode_500(self.driver))

    #drag and drop
    def test26_drag_and_drop(self):
        dragAndDrop_page.click_dnd_tab(self.driver)
        self.assertTrue(dragAndDrop_page.dnd_content_visible(self.driver))


if __name__ == '__main__':
    unittest.main()