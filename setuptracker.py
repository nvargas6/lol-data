#imports
from pathlib import Path
import os
import requests

def extract_summoner_info():
    print('*****')
    request = requests.get('https://127.0.0.1:2999/liveclientdata/sparked_prophet')
    data = request.json()

class SetupTracker:
    def __init__(self, summoner_id, api_key):
        self.summoner_id = summoner_id
        self.api_key = api_key
