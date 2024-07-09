import json
import os
import unittest
from dotenv import load_dotenv
import facebook_page_scraper

load_dotenv()  # take environment variables from .env.

# Set environment variables for Facebook credentials
os.environ['fb_password'] = 'Qwer7890!'
os.environ['fb_email'] = 'edreamsprime3@gmail.com'
# get env password
fb_password = os.getenv('fb_password')
fb_email = os.getenv('fb_email')


class Test_json(unittest.TestCase):

    def is_name_empty(self, dictionary):
        for key in dictionary:
            if dictionary[key]['name'] == "":
                return True
        return False

    def test_scraper_for_json(self):
        scraper = facebook_page_scraper.Facebook_scraper(
            page_or_group_name=None,
            url="https://www.facebook.com/Amazon.fr",
            posts_count=5,
            browser="firefox",
            isGroup=False,
            headless=False,
            username=fb_email,
            password=fb_password
        )
        json_data = scraper.scrap_to_json()
        data_dictionary = json.loads(json_data)

        self.assertEqual(len(data_dictionary), 5)
        self.assertFalse(self.is_name_empty(data_dictionary), "Getting empty strings on name attribute")


class Test_csv_output(unittest.TestCase):

    ''' def test_csv_group(self):
        scraper = facebook_page_scraper.Facebook_scraper(
            page_or_group_name=None,
            url="https://www.facebook.com/profile.php?id=100076420447654",
            posts_count=5,
            browser="firefox",
            isGroup=False,
            headless=False,
            username=fb_email,
            password=fb_password
        )
        was_saved = scraper.scrap_to_csv("group_test", "./")
        self.assertEqual(was_saved, True) '''

    def test_csv_page(self):
        scraper = facebook_page_scraper.Facebook_scraper(
            page_or_group_name=None,
            url="https://www.facebook.com/Amazon.fr",
            posts_count=5,
            browser="firefox",
            headless=False,
            username=fb_email,
            password=fb_password
        )
        was_saved = scraper.scrap_to_csv("meta_test", "./")
        self.assertEqual(was_saved, True)


if __name__ == "__main__":
    unittest.main()