
import random
import string
import requests
import urllib


class SpotifyClient(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_random_tracks(self):
        # %wildcard%
        wildcard = f'%{random.choice(string.ascii_lowercase)}%'
        query = urllib.parse.quote(wildcard)
        offset = random.randint(0, 2000)

        print(query)

        url = f'https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track' 

        response = requests.get(
            url,
            headers={
                # Så vi får en "JSON" Response
                "Content-Type": "application/json"
                "Authorization": f"Bearer {self.api_key}"
            }
        )

        response_json = response.json()

        tracks = [track for track in responese_json['tracks']['items']]

        print(f'Found {len(trakcs)} from your serach')

    def add_trakcs_to_library(self, track_ids):
        url = 'https://api.spotify.com/v1/me/add_trakcs_to_library'

        response = requests.put(
            url,
            headers={
                "Content-Type": "application/json"
                "Authorization": f"Bearer {self.api_key}"
            },
            json={
                'ids': track_ids
            }
        )
        return response.ok
