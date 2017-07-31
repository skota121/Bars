import json
import requests
import sys
import nltk
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

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

#TODO: PRINT ARTIST NAME SO PEOPLE KNOW THEY HAVE THE RIGHT ARTIST

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

titles = [x.lower() for x in titles]
tagged_titles = []

for title in titles:
	tokens = nltk.word_tokenize(title)
	tagged = nltk.pos_tag(tokens)
	tagged_titles.append(tagged)
# Calculate how many times a part of speech shows up
prp_sum = 0
cd_sum = 0
nns_sum = 0
nn_sum = 0
prp_sum = 0
cc_sum = 0
vbp_sum = 0
rb_sum = 0
in_sum = 0
jj_sum = 0
to_sum = 0
dt_sum = 0
pos_sum = 0
for tag in tagged_titles:
	for speech in tag:
		if 'CD' in speech:
			cd_sum += 1
		if 'NNS' in speech:
			nns_sum += 1
		if 'NN' in speech:
			nn_sum +=1
		if 'PRP' in speech:
			prp_sum +=1
		if 'CC' in speech:
			cc_sum +=1
		if 'VBP' in speech:
			vbp_sum +=1
		if 'RB' in speech:
			rb_sum +=1
		if 'IN' in speech:
			in_sum +=1
		if 'JJ' in speech:
			jj_sum +=1
		if 'TO' in speech:
			to_sum +=1
		if 'DT' in speech:
			dt_sum +=1
		if 'POS' in speech:
			pos_sum +=1
# Graphing what we found

objects = ('CD', 'NNS', 'NN', 'PRP', 'CC', 'VBP', 'RB', 'IN', 'JJ', 'TO', 'DT', 'POS')
y_pos = np.arange(len(objects))
performance = [cd_sum, nns_sum, nn_sum, prp_sum, cc_sum, vbp_sum, rb_sum, in_sum, jj_sum, to_sum, dt_sum, pos_sum]
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Usage')
plt.title('Part of Speech Most Commonly Used in Song Names by Artist')
 
plt.show()



























