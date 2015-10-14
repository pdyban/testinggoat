from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard there is a cool new online app
        # for storing lists. She goes online to check out its new homepage
        self.browser.get('http://192.168.0.106:8000')
        self.browser.implicitly_wait(3)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item right away

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock features" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list.
        # Then she sees that the site has generated a unique URL for her -- there is
        # some explanatory text to that effect

        # She visits that URL - her to-do list is still there

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()
