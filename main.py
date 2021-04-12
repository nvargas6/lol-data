import json
import os
import requests
import pandas as pd
from pathlib import Path
from riotwatcher import LolWatcher, ApiError


def absolute_path_test():
    path = os.path.dirname(__file__)
    auth_path = Path(path + '/data/api_key.json')
    with open(auth_path) as file:
        key = json.load(file)
        print(key)
        return key['authkey']


# globals
authkey = absolute_path_test()
api_key_url = '?api_key='

if __name__ == '__main__':
    URL = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/sparked_prophet?api_key=' \
          + authkey

    print(URL)
    print(absolute_path_test())
    request = requests.get(URL)
    print(request)
    data = request.json()
    print(data)

    matchlist_url = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
    URL = matchlist_url + 'ldmTvN5T3T-3GLzJoZ-OggPOiFuYI-aWVkaVFs3QtBniq3wE-NBsl3Dp' + api_key_url + authkey
    print('****')
    print(URL)
    request = requests.get(URL)
    print(request)
    data = request.json()
    print(data)