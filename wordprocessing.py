import spacy


def keyword_extractor(data: list) -> list:
    """Function to implement removal of stopwords and punctuation marks using spacy and return only keywords.
    Add further necessary documentation here."""
    pass


def duplicate_word_removal(data: list) -> list:
    """Function to implement removal of duplicate words present within the list, while maintaining inherent order of
    words in the list. Add further necessary documentation here."""
    pass


def merge_slide_with_same_headers(data: list) -> list:
    """Function to implement merging of slide paragraphs where the slide header is the same. Add further necessary
    documentation here. """
    pass


if __name__ == "__main__":
    data = [{"header": "Dimensionality Reduction PCA",
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
             "paragraph": "Goal is to find a projecRon that captures the largest amount of variaRon in data \
             Find the eigenvectors of the covariance matrix The eigenvectors define the new space",
             "slide": 10}]

    keyword_data = keyword_extractor(data)
    keyword_data = duplicate_word_removal(keyword_data)
    keyword_data = merge_slide_with_same_headers(keyword_data)
