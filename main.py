import json
import os
from pathlib import Path

import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def absolute_path_test():
    path = os.path.dirname(__file__)
    auth_path = Path(path + "/data/api_key.json")
    with open(auth_path) as file:

        #data = json.load(file)
        authkey = json.load(file)
        return authkey["authkey"]
    #auth_path.read_text())

def api_call():
    api_base = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Doublelift?api_key=RGAPI-YOUR-API-KEY"


if __name__ == '__main__':
    print_hi('PyCharm')

    URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/sparked_prophet?api_key=" \
          + absolute_path_test()

    print(URL)
    print(absolute_path_test())
    request = requests.get(URL)
    print(request)
