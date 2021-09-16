"""

File completing step 2: given a pdf document, return a dictionary
of headers and paragraphs

"""


def get_sizes(doc: list) -> list:
    """
    Helper function to get unique sizes within a PDF

    :param doc: The list of blocks within a PDF
    :type: list
    :rtype: list
    :return: a list of unique font sizes
    """
    # ensuring object is not None/empty
    if not doc:
        return []

    unique_fonts = set()
    # for each page in our document
    for page in doc['data']:
        # get the individual text blocks
        for block in page['blocks']:
            # can also get font and color
            unique_fonts.add(round(block['size']))
    # sort the fonts for later filtering
    sorted_fonts = sorted(list(unique_fonts))
    return sorted_fonts


def tag_text(unique_fonts: list, doc: list) -> dict:
    """
    Categorizes each text into either Heading or paragraph.
    Heading includes the top 2 sizes, either title or main heading.
    Paragraph contains all other sizes

    :param unique_fonts: a list of unique fonts in the powerpoint
    :type unique_fonts: list
    :param doc: a list of blocks per each document page
    :type doc: list
    :rtype: dict
    :return: a dictionary categorizing each text into its respective category
    """
    # check that both are not None, or empty
    if not doc or not unique_fonts:
        return {}

    # The Header will be the top 2 font sizes
    # top font size is Title, second would be header
    header_lim = unique_fonts[-2]
    all_pages = []

    for page in doc['data']:
        text_dict = {'Header': "", 'Paragraph': "", 'slide': page['slide']}
        # get the individual text blocks
        for block in page['blocks']:
            # if the text size is smaller than header or title
            if block['size'] < header_lim:
                text_dict['Paragraph'] += block['text'] + " "
            else:
                text_dict['Header'] += block['text'] + " "
        # trim any extra whitespace
        text_dict['Paragraph'] = text_dict['Paragraph'].strip()
        text_dict['Header'] = text_dict['Header'].strip()
        all_pages.append(text_dict)
    return all_pages


def text_to_groupings(doc: list) -> dict:
    """
    Given a pdf document, returns a dictionary of Headers, Paragraphs, and page number

    :param doc: a PDF document containg only words
    :type: list
    :rtype: dict
    :return: a dictionary categorizing each text into its respective category
    """
    font_count = get_sizes(doc)
    dict_fonts = tag_text(font_count, doc)
    return dict_fonts


if __name__ == "__main__":
    pdf_doc = {
        "metadata": {"format": "PDF 1.7",
                     "title": "NCSU Course Syllabus: CSC 422&522",
                     "author": "steffen", "subject": "", "keywords": "",
                     "creator": "Microsoft® Word for Microsoft 365", "producer":
            "Microsoft® Word for Microsoft 365", "creationDate": "D:20210815222418-04'00'",
                     "modDate": "D:20210815222418-04'00'", "trapped": "", "encryption": ""},
        "data": [
            {
                "blocks": [
                    {
                        "text": "Possible title",
                        "size": 14.0
                    }
                ],
                "slide": 1
            },
            {
                "blocks": [
                    {
                        "text":"Possible heading",
                        "size": 12.0
                    },
                    {
                        "text":"Possible subheading",
                        "size": 11.0
                    },
                    {
                        "text":"Possible paragraph",
                        "size": 10.0
                    }
                ],
                "slide": 1
            },
            {
                "blocks": [
                    {
                        "text":"Heading",
                        "size": 12.0
                    },
                    {
                        "text":"Paragraph",
                        "size": 10.0
                    },
                    {
                        "text":"Another Heading",
                        "size": 12.0
                    }
                ],
                "slide": 2
            }
        ]
    }
    my_dict = text_to_groupings(pdf_doc)
    print(my_dict)
