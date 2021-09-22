import shutil
import pyfiglet
import sys
from extract_sizes import extract_words, text_to_groupings
import wordprocessing as wp
from rapidapi_search import rapid_search
from google_search import search_call, get_people_also_ask_links
import time
import concurrent.futures


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
    file = "../data/lecture4.pdf"
    raw_data = extract_words(file)
    raw_data = text_to_groupings(raw_data)
    keyword_data = wp.extract_noun_chunks(raw_data)
    keyword_data = wp.merge_slide_with_same_headers(keyword_data)
    keyword_data = wp.duplicate_word_removal(keyword_data)
    search_query = wp.construct_search_query(keyword_data)
    print(search_query)
    print(len(search_query))

    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(get_people_also_ask_links, search_query[:20])
    print(time.time() - start)
    for result in results:
        print(result)