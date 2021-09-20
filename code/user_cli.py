import shutil
import pyfiglet
import sys
import fitz
from extract_sizes import extract_words, text_to_groupings
import wordprocessing as wp
from rapidapi_search import rapid_search
import pprint
import re
from google_search import search_call, get_people_also_ask_links


def user_menu():
    format_welcome_message = pyfiglet.figlet_format("LECTURE AID")
    size = shutil.get_terminal_size(fallback=(120, 50))
    valid_choices = ["1", "2", "Q", "q"]
    print(format_welcome_message.center(size.columns) + "\n")
    print("Welcome to Lecture Aid. Choose from the following options:\n")
    print("Option 1: Press 1 to enter the file location you would like Lecture Aid to help you find resources on.")
    print("Option 2: Press 2 ")
    print()
    print("Press Q to quit the program.")

    while True:
        choice = input("Please Enter your choice:")[0]
        if choice in valid_choices:
            break
        else:
            print("That choice is not available now. Please try again")
            continue

    if choice == valid_choices[0]:
        file = input("Please enter the path to the file: ")
        return file

    elif choice == valid_choices[1]:
        input("")

    elif (choice == valid_choices[-1] or choice == valid_choices[-2]):
        print("Thank you for using Lecture Aid. Closing Program now.")
        sys.exit(0)


if __name__ == "__main__":
    # file = user_menu()
    file = "../data/lec7.pdf"
    raw_data = extract_words(file)
    raw_data = text_to_groupings(raw_data)
    keyword_data = wp.merge_slide_with_same_slide_number(wp.keyword_extractor(raw_data))
    keyword_data = wp.duplicate_word_removal(wp.merge_slide_with_same_headers(keyword_data))
    print_file = "Results for " + file + "\n" + "=============================== \n"

    for data in keyword_data:
        header_and_para = data['Header_keywords'] + data['Paragraph_keywords']
        header_and_para = [data for data in header_and_para if len(data) >= 3]
        query = " ".join(header_and_para)
        print_file += "Query Words \n"
        print_file += query + "\n"
        print_file += "Slide Numbers \n"
        print_file += str(data["slides"]) + "\n"
        people_also_ask_result = get_people_also_ask_links(query)
        query_result_data = search_call(query)
        print_file += "People Also Ask Results \n"
        print_file += str(people_also_ask_result) + "\n"
        print_file += "Google Search Results \n"
        print_file += str(query_result_data) + "\n"
    with open("Result2.txt", mode="w") as f:
        f.write(print_file)