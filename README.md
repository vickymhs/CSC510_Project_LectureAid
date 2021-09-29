![GitHub](https://img.shields.io/github/license/mtkumar123/CSC510_Project_LectureAid)
[![Build Status](https://app.travis-ci.com/mtkumar123/CSC510_Project_LectureAid.svg?branch=main)](https://app.travis-ci.com/mtkumar123/CSC510_Project_LectureAid)
[![codecov](https://codecov.io/gh/mtkumar123/CSC510_Project_LectureAid/branch/main/graph/badge.svg?token=EEGIC8T7QM)](https://codecov.io/gh/mtkumar123/CSC510_Project_LectureAid)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5528349.svg)](https://doi.org/10.5281/zenodo.5528349)
![Top Language](https://img.shields.io/github/languages/top/mtkumar123/CSC510_Project_LectureAid)
![GitHub issues](https://img.shields.io/github/issues-raw/mtkumar123/CSC510_Project_LectureAid)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/mtkumar123/CSC510_Project_LectureAid)
<!-- ![GitHub forks](https://img.shields.io/github/forks/mtkumar123/CSC510_Project_LectureAid?style=social)
 -->
# Project Lecture AID

This repo contains the code for Lecture Aid [v1.0.0](https://github.com/mtkumar123/CSC510_Project_LectureAid/releases/tag/v1.0.0), a project for CSC510 Fall 21. 

# What is Project Lecture AID?

After a long class, ever had to come back home and google everything you supposedly learnt from the lecture handout for that day's class? Ever spend ~30-45 minutes just to search through google and compile a list of websites that explain what you need? And then a month later when midterms are around a corner, ever spend that same 30-45 minutes trying to find those websites again cause you forgot to bookmark them? 

Project Lecture AID hopes to solve that hassle for you. 

Upload your lecture pdf to our user based terminal menu, and Lecture AID will extract the text, process it, and search the internet for key topics from that lecture. Once it finds relevant results, Lecture AID opens up a browser window with a list of questions relevant to your topic, and website links that should answer said questions, and also a wordcloud that highlights key words in the lecture. 

# Technologies Used

Text Extraction from pdfs was done with the help of PyMuPDF. Documentation can be viewed here:
https://pymupdf.readthedocs.io/en/latest/

Word Processing Logic was done with the help of Spacy. Documentation can be viewed here:
https://spacy.io/api/doc

# Requirements
- Python (atleast 3.8) and pip
- [Microsoft Visual C++ Build tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- Using pip install 
  - google-api-python-client, version 2.22.0
  - people_also_ask, version 0.0.6
  - spacy, version 3.1.2 or greater
  - spacy-legacy, version 3.0.8
  - en_core_web_lg-3.1.0
  - pyfiglet, version 0.8.post1
  - PyMuPDF, version 1.18.19
  - wordcloud, version 1.8.1
  - matplotlib, version 3.4.3

# Setup
- run `pip install -r requirements.txt`
  - this installs all of the required python libraries

# How to run


User uploads the lecture pdf through the terminal menu, Lecture Aid process the pdf and provides relevant results in questions and answers format through a browser window.

- Step 1: User Terminal Menu: (`python code/user_cli.py`)

![1](https://user-images.githubusercontent.com/89501363/135198847-bf568a48-fa0b-4bfc-9e83-1b793b07d800.PNG)

- Step 2: Press 1 to enter a pdf. Enter the path of the PDF to be uploaded, ( Upload any lecture PDF with relevant contents )

![2](https://user-images.githubusercontent.com/89501363/135198927-2fb98b67-4de8-460f-9f25-100d65dfa310.PNG)

- Step 3: Browser Window displaying the search results and word cloud for the pdf uploaded.

![3](https://user-images.githubusercontent.com/89501363/135200016-e0214363-772d-4e6e-918e-bada1fcdfed3.PNG)


# Troubleshooting
- When running the code/tests, I'm getting a `no such module named code` error?
  - Try prefixing the command with `python -m`, for example, `python -m pytest`
- When I try to run pip install, I'm getting an error for wordcloud relating to Microsoft C++?
  - Microsoft C++ build tools are needed to generate the wordcloud. See the requirements section for the download link.

# Future work
- #### Build a website for a GUI interface for the user
  Our project is currently using a command line interface to get input, and output a .html file. A roadmap item would be to implement a website   instead. This way the user would open up the Lecture Aid website, be able to add a file to the website, and click a button to process the file. Then, the website would display the results (wordcloud and question and answers). This will make it easier for users to use the project, without having to download/execute code locally.
  
- #### Support for additional file types
  Currently the project supports only PDF format for the uploaded files. In future other formats such as .ppt, .doc should be supported
 
- #### Increase the concurrency efficiency
  Currently, we are using the maximum number of threads (10) for running search queries, but could still be room for improvement using other multithreading/multiprocessing tools.
  
- #### Improve Word Extraction Logic
  Currently Spacy is being used to extract noun phrases from each slide/page of the document. Then the high frequency noun phrases are calculated and used in the final search query. However this causes an issue when every slide has the document’s author name and email address listed. The author name is considered as a noun phrase, and since it appears on every slide has a high frequency, and thus appears on the final search query.

- #### Save favourite links to bookmarks
  A button can be added beside each link in the results to save those links to browser bookmarks.
  
- #### Build a browser extension
  Build a browser extension which lets the user to select text from a webpage and send a request to the application and get the links of pdf webpages.

# Contact Us
   E-mail: lectureaidnscu@gmail.com
