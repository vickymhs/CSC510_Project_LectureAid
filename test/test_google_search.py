import unittest
from code.google_search import get_people_also_ask_links
import json

class TestGoogleSearch(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_get_people_also_ask_links_type_check(self):
        """Test the get_people_also_ask_links method and checks type"""
        test = "principal components"
        result = get_people_also_ask_links(test)
        self.assertEqual(list, type(result))

    def test_get_people_also_ask_links_data_check(self):
        """Test the get_people_also_ask_links method and checks data"""
        filename = "./test/data/people_also_ask_links_results.json"
        with open(filename, encoding='utf-8') as file_pointer:
            doc = json.load(file_pointer)
            test = "Continuous integration"
            result = get_people_also_ask_links(test)
            self.assertEqual(result, doc)

    def test_get_people_also_ask_links_empty_data_check(self):
        """Test the get_people_also_ask_links method with empty string and checks data"""
        test = ""
        result = get_people_also_ask_links(test)
        self.assertEqual(result, [])