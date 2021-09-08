import unittest
import sys
sys.path.append("../code")
from step1 import get_doc
from step2 import get_sizes, tag_text, text_to_groupings


class MyTestCase(unittest.TestCase):

    def test_font_doc_none(self):
        # assert when no document is passed, it returns none
        unique_fonts = get_sizes(None)
        self.assertIsNone(unique_fonts)

    def test_dict_fonts_none(self):
        # assert when no document is passed, it returns none
        dict_none = tag_text(None)
        self.assertIsNone(dict_none)

    def test_font_size_1(self):
        filename = "data/Test_1.pdf"
        doc = get_doc(filename)
        actual_fonts = get_sizes(doc)

        expected_fonts = [12, 28, 44, 60]
        self.assertEqual(expected_fonts, actual_fonts)

    def test_text_to_groupings_1(self):
        filename = "data/Test_1.pdf"
        doc = get_doc(filename)
        actual_dict = text_to_groupings(doc)

        # check the text
        page1 = {'Header': 'Test 1 : Computer Science', 'Paragraph': '', 'slide': 0}
        page2 = {'Header': 'Large Heading', 'Paragraph': 'Medium text Small text', 'slide': 1}
        page3 = {'Header': 'Large Heading 2', 'Paragraph': 'Medium text 2 Small text 2', 'slide': 2}
        expected = [page1, page2, page3]
        self.assertEqual(expected[0], actual_dict[0], "Page 0")
        self.assertEqual(expected[1], actual_dict[1], "Page 1")
        self.assertEqual(expected[2], actual_dict[2], "Page 2")
        self.assertEqual(expected, actual_dict)


if __name__ == '__main__':
    unittest.main()
