from datetime import datetime

from requests.models import requote_uri
from pipecrmdeal import create_new_deal
from typing import List

import requests

from gitgist import GitGist

USER_GISTS_API = "https://api.github.com/users/{}/gists"
SINCE_DATE_PARAMETER = "?since={}"


class GistsClient:

    def __init__(self):
        pass

    def fetch_gists(self, username: str, since_date: str = None) -> List[GitGist]:
        gists_api_response = requests.get(self.get_gists_url(username, since_date))

        if gists_api_response:
            return [GitGist.from_json(gist) for gist in gists_api_response.json()]  
            
        return []
   
    def get_gists_url(self, username: str, since_date: str) -> str:
        request_url = USER_GISTS_API.format(username)

        return request_url if not since_date else request_url + SINCE_DATE_PARAMETER.format(since_date)
