"""

File completing step 2: given a pdf document, return a dictionary
of headers and paragraphs

"""
import sys
from step1 import get_doc

page_blocks = []


def get_sizes(doc):
    """
    Helper function to get unique sizes within a PDF

    :param doc: The list of blocks within a PDF
    :type: list
    :rtype: list
    :return: a list of unique font sizes
    """
    unique_fonts = set()
    if doc is None:
        return None
    # for each page in our document
    for page in doc:
        # get the individual text blocks
        for block in page['blocks']:
            # can also get font and color
            unique_fonts.add(round(block['size']))
    # sort the fonts for later filtering
    sorted_fonts = sorted(list(unique_fonts))
    return sorted_fonts


def tag_text(unique_fonts, doc):
    """
    Categorizes each text into L, M, or S.

    :param unique_fonts: a list of unique fonts in the powerpoint
    :type unique_fonts: list
    :param doc: a list of blocks per each document page
    :type doc: list
    :rtype: dict
    :return: a dictionary categorizing each text into its respective category
    """
    if unique_fonts is None or len(unique_fonts) == 0:
        return None
    if doc is None or len(doc) == 0:
        return None

    # The Header will be the top 2 font sizes
    # top font size is Title, second would be header
    header_lim = unique_fonts[-2]
    all_pages = []

    for page in doc:
        text_dict = {'Header': "", 'Paragraph': "", 'slide': page['slide']}
        # get the individual text blocks
        for block in page['blocks']:
            # if the text size is smaller than header or title
            if block['size'] < header_lim:
                text_dict['Paragraph'] += block['text']
            else:
                text_dict['Header'] += block['text']
        all_pages.append(text_dict)
    return all_pages


def text_to_groupings(doc):
    """
    Given a pdf document, returns a dictionary of Headers, Paragraphs, and page number

    :param doc: a PDF document containg only words
    :rtype: dict
    :return: a dictionary categorizing each text into its respective category
    """
    font_count = get_sizes(doc)
    dict_fonts = tag_text(font_count, doc)
    return dict_fonts


if __name__ == "__main__":
    filename = sys.argv[1]
    pdf_doc = get_doc(filename)
    my_dict = text_to_groupings(pdf_doc)
    print(my_dict)
