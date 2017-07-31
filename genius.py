
import json
import requests
import sys

headers = {'Authorization': 'Bearer TOKEN'}
song = sys.argv[1]
baseUrl = 'https://api.genius.com'
## Search for Song and Return Artist
url = baseUrl +'/search'

data = {'q': song}

# Make post request for searched song
d = requests.get(url= url, data = data, headers= headers)
song_json = d.json()

# Parse song_json for artist id
artist_id = song_json["response"]["hits"][0]["result"]["primary_artist"]["id"]

