from googleapiclient.discovery import build
import json
import configparser
import people_also_ask
import re

# requires pip install google-api-python-client

# Global variables for search request
API_KEY = "api_key"
CSE_ID = "cse_id"
SEARCH_COUNT = 5

# Initialize config parameters
config = configparser.ConfigParser()
config.read('config/search_api_config.cfg')

def getCredentials(key):
    """
    Returns the sensitive credentials from the configuration files
    :param key: The key for the credential value
    :return: The authenticate value for the key

    """
    key_map = {'api_key' : config['credentials']['api_key'],'cse_id' : config['credentials']['cse_id']}
    if(key_map[key]):
        return key_map[key]
    else:return -1


def google_search(search_term: str, api_key: str, cse_id: str, **kwargs) -> json:
   """

   Perform a Google search using Custom Search API
   :param search_term: The param represents the search strings for the web search
   :param api_key: Represents the credentials for API hit
   :param cse_id: Represents the credentials for API hit
   :return: The web search API response in JSON format

   """
   # Build request
   service = build("customsearch", "v1", developerKey=api_key)
   # Execute request
   query_result = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
   return query_result


# Call for the Web search
def search_call(search_term) -> json:
    """
        Returns the sensitive credentials from the configuration files
        :param key: The key for the credential value
        :return: The authenticate value for the key
    """

    query_result = google_search(search_term, getCredentials(API_KEY), getCredentials(CSE_ID), num = SEARCH_COUNT)
    links = []
    for item in query_result["items"]:
        links.append(item["formattedUrl"])
    return links

def get_people_also_ask_links(search_term):
    rel_qns = people_also_ask.get_related_questions(search_term)
    result = []
    if rel_qns:
        for rel_qn in rel_qns:
            question = re.search(r"[^?]*", rel_qn).group(0) + "?"
            answer = people_also_ask.get_answer(question)
            if answer["has_answer"]:
                result.append({"Question": answer["question"], "Answer": answer["link"]})
    return result

# Store result
# with open('venv/output_data.txt', 'w') as output_file:
#         json.dump(query_result, output_file)