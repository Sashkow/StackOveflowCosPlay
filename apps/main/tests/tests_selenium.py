import unittest

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class SeleniumTestCase(LiveServerTestCase):
    """
    A base test case for Selenium, providing hepler methods for generating
    clients and logging in profiles.
    """

    def open(self, url):
        print self.live_server_url
        # self.wd.get("%s%s" % (self.live_server_url, url))

    def test_smth(self):
        print self.live_server_url

        



# class RegisterTestCase(unittest.TestCase):
#     """
#     Test the following user story:
#       - go to register page
#       - fill fields
#       - submit
#       - check reaction (for valid and invalid data)
#     """

#     def setUp(self):        
#         self.driver = webdriver.Firefox()
#         # self.url = "http://127.0.0.1:8000/"

#     def test_valid_data(self):
#         """
#         test when user enters correct data
#         """
#         self.driver.get(self.url)
        
#         assert "Main Page" in self.driver.title
#         elem = self.driver.find_element_by_name("edit_page_link")
#         elem.click()
#         assert "Edit Page" in self.driver.title
#         elem = self.driver.find_element_by_id("id_name")
#         elem.clear()
#         elem.send_keys("NewValue")
#         elem = self.driver.find_element_by_name("save_and_back_submit")
#         elem.click()
#         assert "..." in elem.get_attribute("value")
        

#     def test_invalid_data(self):
#         """ test when user enters INcorrect data """
#         self.driver.get(self.url)
#         assert "Main Page" in self.driver.title
#         elem = self.driver.find_element_by_name("edit_page_link")
#         elem.click()
#         assert "Edit Page" in self.driver.title
#         elem = self.driver.find_element_by_id("id_email")
#         elem.clear()
#         elem.send_keys("BadEmail")
#         elem = self.driver.find_element_by_name("save_and_back_submit")
#         elem.click()
#         assert "Edit Page" in self.driver.title
        
#     def tearDown(self):
#         self.driver.close()


# class LoginTest(unittest.TestCase):
#     """
#     Test the following user story:
#       - go to main page
#       - go to edit page
#       - edit data
#       - return to main page
#       - see data changed 
#     """

#     def setUp(self):        
#         self.driver = webdriver.Firefox()
#         self.url = "http://127.0.0.1:8000/"

#     def test_valid_data(self):
#         """
#         test when user enters correct data
#         """
#         self.driver.get(self.url)
        
#         assert "Main Page" in self.driver.title
#         elem = self.driver.find_element_by_name("login_page_link")
#         elem.click()
#         assert "Login Page" in self.driver.title

#         elem = self.driver.find_element_by_id("id_username")
#         elem.clear()
#         elem.send_keys("leela")

#         elem = self.driver.find_element_by_id("id_password")
#         elem.clear()
#         elem.send_keys("leela")

#         elem = self.driver.find_element_by_name("login_submit")
#         elem.click()
#         assert "Main Page" in self.driver.title
#         assert "Name: Leela" in self.driver.page_source
        
#     def tearDown(self):
#         self.driver.close()


# if __name__ == "__main__":
#     unittest.main()
