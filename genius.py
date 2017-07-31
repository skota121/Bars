
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


# Send another request to get songs written by an artist

songs_url = 'https://api.genius.com/artists/{}/songs'.format(artist_id)

songsbyartist = requests.get(url=songs_url, headers=headers)

# Parse JSON again
songs = songsbyartist.json()

songs = songs["response"]["songs"]


# Collect all the Song Titles and append to a list
titles = []
for song in songs:
	titles.append(song["title"].encode('ascii'))
print titles 