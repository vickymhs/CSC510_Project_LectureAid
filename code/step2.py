"""

File completing step 2: given a pdf document, return a dictionary
of headers and paragraphs

"""
import sys
# to be replaced with what step1 is returning
from step1 import get_doc

page_blocks = []


def get_sizes(doc):
    """
    Helper function to get unique sizes within a PDF

    :param doc: The PDF document
    :rtype: list
    :return: a list of unique font sizes
    """
    block_is_text = 0
    unique_fonts = set()
    if doc is None:
        return None
    # for each page in our document
    for page in doc:
        # get the descriptive dictionary
        blocks = page.getText("dict")["blocks"]
        # save for later methods
        page_blocks.append(blocks)

        for block in blocks:
            if block['type'] == block_is_text:
                for line in block["lines"]:
                    for text in line["spans"]:
                        # can also get font and color
                        unique_fonts.add(round(text['size']))
    # sort the fonts for later filtering
    sorted_fonts = sorted(list(unique_fonts))
    return sorted_fonts

def tag_text(unique_fonts):
    """
    Categorizes each text into L, M, or S.

    :param unique_fonts: a list of unique fonts in the powerpoint
    :type unique_fonts: list
    :rtype: dict
    :return: a dictionary categorizing each text into its respective category
    """
    if unique_fonts is None or len(unique_fonts) == 0:
        return None

    # The Header will be the top 2 font sizes
    # top font size is Title, second would be header
    header_lim = unique_fonts[-2]
    all_pages = []

    for idx, blocks in enumerate(page_blocks):
        text_dict = {'Header': "", 'Paragraph': "", 'slide': idx}
        # each blocks is a page.
        # a blocks can have multiple text blocks (think header, paragraph, etc)
        for block in blocks:
            if block['type'] == 0:  # this block contains text
                # for each line within our text block
                for line in block["lines"]:
                    # each line contains a span element which actually contains the text
                    for span in line["spans"]:
                        text = span['text'].strip()   # removing whitespaces
                        # if the text is not empty
                        if text:
                            # if the text size is smaller than header or title
                            if span['size'] < header_lim:
                                text_dict['Paragraph'] += text
                            else:
                                text_dict['Header'] += text
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
    dict_fonts = tag_text(font_count)
    return dict_fonts


if __name__ == "__main__":
    filename = sys.argv[1]
    pdf_doc = get_doc(filename)
    my_dict = text_to_groupings(pdf_doc)
    print(my_dict)
