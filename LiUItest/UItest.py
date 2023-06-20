import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestRPNCalculator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_form_displayed_correctly(self):
        self.driver.get('http://localhost:5000')
        input_field = self.driver.find_element(By.ID, 'tokens')
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

        self.assertEqual(input_field.is_displayed(), True)
        self.assertEqual(submit_button.is_displayed(), True)

    def test_valid_expression_is_calculated_correctly(self):
        self.driver.get('http://localhost:5000')
        input_field = self.driver.find_element(By.ID, 'tokens')
        input_field.send_keys('2, 3, +')
        input_field.send_keys(Keys.RETURN)
        result_div = self.driver.find_element(By.XPATH, '//p[contains(@class, "result")]')

        self.assertEqual(result_div.text.strip(), '5')

    def test_error_message_is_shown_for_invalid_input(self):
        self.driver.get('http://localhost:5000')
        input_field = self.driver.find_element(By.ID, 'tokens')
        input_field.send_keys('2, 3, foo')
        input_field.send_keys(Keys.RETURN)
        error_div = self.driver.find_element(By.XPATH, '//p[contains(@class, "error")]')

        self.assertIn('Invalid token: foo', error_div.text)

    def tearDown(self):
        self.driver.quit()
