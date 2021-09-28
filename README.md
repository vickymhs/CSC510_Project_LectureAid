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

This repo contains the code for Lecture Aid, a project for CSC510 Fall 21. 

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

# Setup
- run `pip install -r requirements.txt`
  - this installs all of the required python libraries

# How to run
- `python code/user_cli.py`
- Press 1 to enter a pdf
  - Future work includes pressing 2 for pptx
- Enter the path to your pdf file
- The results are stored in results.txt
- A wordcloud is generated as a png file

# Troubleshooting
- When running the code/tests, I'm getting a `no such module named code` error?
  - Try prefixing the command with `python -m`, for example, `python -m pytest`
- When I try to run pip install, I'm getting an error for wordcloud relating to Microsoft C++?
  - Microsoft C++ build tools are needed to generate the wordcloud. See the requirements section for the download link.

# Future work
- Include more than pdf
- Have a website instead
- Speed up the program

