import json
import requests
import configparser
import people_also_ask

# Global variables for search request
API_KEY = "rapid_api_key"
SEARCH_COUNT = 5

# Initialize config parameters
config = configparser.ConfigParser()
config.read('config/search_api_config.cfg')


def rapid_search(search_term: str) -> json:
    """

    Perform a search using Rapid Search API

    :param search_term: The param represents the search strings for the web search
    :param api_key: Represents the credentials for API hit
    :return: The web search API response in JSON format

    """
    head = {'x-rapidapi-host': 'contextualwebsearch-websearch-v1.p.rapidapi.com',
            'x-rapidapi-key': config['credentials']['rapid_api_key']}
    param = {'q': search_term, 'pageNumber': '1', 'pageSize': SEARCH_COUNT, 'autoCorrect': 'true'}
    res = requests.get('https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI', params=param,
                       headers=head)
    obj = res.json()
    urls = []
    for i in obj['value']:
        urls.append(i['url'])
    rel_qns = people_also_ask.get_related_questions(search_term)
    for qn in rel_qns:
        param = {'q': qn, 'pageNumber': '1', 'pageSize': 1, 'autoCorrect': 'true'}
        rel_url = (requests.get('https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI', params=param,
                       headers=head))
        rel_obj = rel_url.json()
        for i in rel_obj['value']:
            urls.append(i['url'])
    url_json = json.dumps(urls)
    return url_json
