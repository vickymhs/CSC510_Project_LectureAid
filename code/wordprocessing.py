from collections import OrderedDict
import sys
import spacy


def keyword_extractor(data: list) -> list:
    """Function to implement removal of stopwords and punctuation marks using spacy and return only keywords.
    Add further necessary documentation here."""
    try:
        nlp = spacy.load("en_core_web_lg")
    except OSError as e:
        print("Please make sure you have Spacy Word Model en_core_web_lg downloaded.")
        print(e)
        sys.exit()
    pos_tag = ["NOUN"]
    for slide in data:
        doc_header = nlp(slide["header"].lower())
        doc_paragraph = nlp(slide["paragraph"].lower())
        header_keywords = []
        paragraph_keywords = []
        for token in doc_header:
            if token.text in nlp.Defaults.stop_words or token.is_punct:
                continue
            if token.pos_ in pos_tag:
                header_keywords.append(token.text)
        for token in doc_paragraph:
            if token.text in nlp.Defaults.stop_words or token.is_punct:
                continue
            if token.pos_ in pos_tag:
                paragraph_keywords.append(token.text)
        slide["header_keywords"] = header_keywords
        slide["paragraph_keywords"] = paragraph_keywords
    return data


def duplicate_word_removal(data: list) -> list:
    """Function to implement removal of duplicate words present within the list, while maintaining inherent order of
    words in the list. Add further necessary documentation here."""
    for dictionary in data:
        dictionary['header_keywords'] = list(OrderedDict.fromkeys(dictionary['header_keywords']))
        dictionary['paragraph_keywords'] = list(OrderedDict.fromkeys(dictionary['paragraph_keywords']))
    return data


def merge_slide_with_same_headers(data: list) -> list:
    """Function to implement merging of slide paragraphs where the slide header is the same. Add further necessary
    documentation here. """
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