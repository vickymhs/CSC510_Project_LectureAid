import unittest
from code.wordprocessing import keyword_extractor, duplicate_word_removal, merge_slide_with_same_headers


class TestWordProcessing(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_keyword_extractor(self):
        data = [{"Header": "This is a Header", "Paragraph": "This is a Paragraph", "slide": 10}]
        keywords = keyword_extractor(data)
        data[0]["Header_keywords"] = ["header"]
        data[0]["Paragraph_keywords"] = ["paragraph"]
        self.assertEqual(keywords, data)

    def test_duplicate_word_removal(self):
        data = [{"Header": "This is a Header, and this is a Header", "Paragraph": "This is a Paragraph, and this is a "
                                                                                  "Paragraph",
                 "Header_keywords": ["header", "header"],
                 "Paragraph_keywords": ["paragraph", "paragraph"], "slide": 10}]
        remove_duplicates = keyword_extractor(data)
        data[0]["Header_keywords"] = ["header"]
        data[0]["Paragraph_keywords"] = ["paragraph"]
        self.assertEqual(data, remove_duplicates)

    def test_merge_slide_with_same_header(self):
        data = [{"Header": "This is a Header", "Paragraph": "This is paragraph one", "Header_keywords": ["header"],
                 "Paragraph_keywords": ["paragraph", "one"], "slide": 10},
                {"Header": "This is a Header", "paragraph": "This is paragraph two", "Header_keywords": ["header"],
                 "Paragraph_keywords": ["paragraph", "two"], "slide": 11}]
        merged_data = merge_slide_with_same_headers(data)
        data[0]["slides"] = [10, 11]
        data[0]["Paragraph_keywords"] = ["paragraph", "one", "paragraph", "two"]
        data[0].pop("Paragraph", None)
        data[0].pop("slide", None)
        data.pop()
        self.assertEqual(data, merged_data)


if __name__ == "__main__":
    unittest.main()
