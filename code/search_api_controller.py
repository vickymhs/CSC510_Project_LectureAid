from google_search import *
# from rapidapi_search import *
if __name__ == "main":
    # Response of the Google web API Search
    google_search_results = search_call("model in ruby")

    # Response of the Rapid web API Search
    # rapidapi_search_results = search_call("model in ruby")

    # Response of the combined API Search
    linkSet = google_search_results
    print(linkSet)
    # print(rapidapi_search_results)
