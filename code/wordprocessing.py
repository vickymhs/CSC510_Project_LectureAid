from collections import OrderedDict
import sys
import spacy
import re


def keyword_extractor(data: list) -> list:
    """
    Function to extract keywords from the headers and paragraphs of slides
    :param data: The list of dictionaries of the form [{"header":"", "paragraph":"", slide:int}]
    :return: The list of dictionaries with keywords extracted of the form [{"header":"", "paragraph":"",
             "header_keywords": [], "paragraph_keywords": [], slide:int}]
    """
    try:
        nlp = spacy.load("en_core_web_lg")
    except OSError as e:
        print("Please make sure you have Spacy Word Model en_core_web_lg downloaded.")
        print(e)
        sys.exit()
    pos_tag = ["PROPN", "NOUN"]
    for slide in data:
        doc_header = nlp(slide["header"].lower())
        doc_paragraph = nlp(slide["paragraph"].lower())
        header_keywords = []
        paragraph_keywords = []
        for token in doc_header:
            if token.text in nlp.Defaults.stop_words or token.is_punct:
                continue
            if token.pos_ in pos_tag:
                word = re.sub(r"[^0-9a-zA-Z]+", "", token.text)
                if word != "":
                    header_keywords.append(word)
        for token in doc_paragraph:
            if token.text in nlp.Defaults.stop_words or token.is_punct:
                continue
            if token.pos_ in pos_tag:
                word = re.sub(r"[^0-9a-zA-Z]+", "", token.text)
                if word != "":
                    paragraph_keywords.append(word)
        slide["header_keywords"] = header_keywords
        slide["paragraph_keywords"] = paragraph_keywords
    return data


def duplicate_word_removal(data: list) -> list:
    """

    :param data: The list of dictionaries of the form [{"header":"", "header_keywords": [],
                "paragraph_keywords": [], slides:[int]}]
    :return: The list of dictionaries with duplicate keywords removed of the form [{"header":"", "header_keywords": [],
                "paragraph_keywords": [], slides:[int]}]
    """
    for dictionary in data:
        dictionary['header_keywords'] = list(OrderedDict.fromkeys(dictionary['header_keywords']))
        dictionary['paragraph_keywords'] = list(OrderedDict.fromkeys(dictionary['paragraph_keywords']))
    return data


def merge_slide_with_same_headers(data: list) -> list:
    """

    :param data: The list of dictionaries of the form [{"header":"", "paragraph":"", "header_keywords": [],
                "paragraph_keywords": [], slide:int}]
    :return: The list of dictionaries where slides containing the same header are merged
             of the form [{"header":"", "header_keywords": [], "paragraph_keywords": [], slides:[int]}]
    """
    merged = []
    headers = []
    for slide in data:
        if slide["header"] not in headers:
            headers.append(slide["header"])
            paragraph_keywords = []
            slide_numbers = []
            for x in [y for y in data if y["header"] == slide["header"]]:
                paragraph_keywords += x["paragraph_keywords"]
                slide_numbers.append(x["slide"])
            merged.append({"header": slide["header"], "header_keywords": slide["header_keywords"],
                           "paragraph_keywords": paragraph_keywords, "slides": slide_numbers})
    return merged


def merge_slide_with_same_slide_number(data: list) -> list:
    '''

    :param data:
    :return:
    '''
    merged = []
    slide_number = []
    for slide in data:
        if slide["slide"] not in slide_number:
            slide_number.append(slide["slide"])
            header_keywords = []
            paragraph_keywords = []
            for x in [y for y in data if y["slide"] == slide["slide"]]:
                header_keywords += x["Header_keywords"]
                paragraph_keywords += x["Paragraph_keywords"]
            merged.append({"Header": slide["Header"], "Header_keywords": header_keywords,
                           "Paragraph_keywords": paragraph_keywords,
                           "slide": slide["slide"]})
    return merged


if __name__ == "__main__":
    main_data = [{"header": "Dimensionality Reduction PCA",
                  "paragraph": "Dimensionality Reduction Purposes: – Avoid curse of dimensionality – Reduce amount \
            of time and memory required by data mining algorithms Allow data to be more easily \
            visualized May help to eliminate irrelevant features or reduce noise Techniques Principal Component Analysis \
            Singular Value Decomposition supervised and non-linear techniques",
                  "slide": 8},
                 {"header": "Gratuitous ARP",
                  "paragraph": "Every machine broadcasts its mapping when it boots to update ARP caches in other machines \
            n Example: A sends an ARP Request with its own IP address as the target IP address \
            n Sender MAC=MACA, Sender IP=IPA n Target MAC=??, Target IP=IPA \
            n What if a reply is received?",
                  "slide": 9},
                 {"header": "Dimensionality Reduction PCA",
                  "paragraph": "Goal is to find a projection that captures the largest amount of variation in data \
             Find the eigenvectors of the covariance matrix The eigenvectors define the new space",
                  "slide": 10}]

    keyword_data = keyword_extractor(main_data)
    print(keyword_data)
    keyword_data = merge_slide_with_same_headers(keyword_data)
    print(keyword_data)
    keyword_data = duplicate_word_removal(keyword_data)
    print(keyword_data)
