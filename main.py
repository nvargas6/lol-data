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
accountID = 'ldmTvN5T3T-3GLzJoZ-OggPOiFuYI-aWVkaVFs3QtBniq3wE-NBsl3Dp'
summonerID = 'gG_Y0RKhz3nLMMu8aNhnGjni0svFGaA02lyfkKLsN-CMNrKB'
ppuuid = 'UMGFI8uYS72cjgB2GAe24p1jFZ58-5TeBXkVC0-K3LBQAEDyzcltSrS4pWC_4Cvg4dSuy3ADXSwccQ'

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
    #   print(data)

    #match_url = 'https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/' + summonerID \
    #            + api_key_url + authkey

    match_url = 'https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/' + summonerID \
                + api_key_url + authkey

    print('\n*********\n')
    print(match_url)
    request = requests.get(match_url)
    print(request)
    data = request.json()
    print(data)

    #calls name of active player
    name = requests.get('https://127.0.0.1:2999/liveclientdata/activeplayername')
    live_data = requests.get('https://127.0.0.1:2999/liveclientdata/' + name)
    print('\n*********\n')
    print(live_data)
    request = requests.get(match_url)
    print(request)
    data = request.json()
    print(data)
