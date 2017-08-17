	import json
	from bs4 import BeautifulSoup
	import urllib2
	from watson_developer_cloud import NaturalLanguageUnderstandingV1
	import watson_developer_cloud.natural_language_understanding.features.v1 \
	  as Features
	import sys


	natural_language_understanding = NaturalLanguageUnderstandingV1(username="", password="", version="2017-02-27")

	baseUrl = 'http://www.azlyrics.com/lyrics/{}/{}.html'.format(sys.argv[1],sys.argv[2])
	result = urllib2.urlopen(baseUrl).read()
	soup = BeautifulSoup(result, 'html.parser')
	letters = soup.find_all("div")
	for i in soup.find_all("i"):
		i.decompose()

	letters = letters[21]

	lyrics = letters.text

	response = natural_language_understanding.analyze(text= lyrics, features=[ Features.Emotion()])

	response_anger = response["emotion"]["document"]["emotion"]["anger"]
	response_joy  = response["emotion"]["document"]["emotion"]["joy"]
	response_sadness = response["emotion"]["document"]["emotion"]["sadness"]
	response_fear = response["emotion"]["document"]["emotion"]["fear"]
	response_disgust = response["emotion"]["document"]["emotion"]["disgust"]

	print 'The song, {}, by {} had the following emotions:'.format(sys.argv[2].title(),sys.argv[1].title())
	print 'Anger:', response_anger  
	print 'Sadness:', response_sadness
	print 'Disgust:', response_disgust
	print 'Fear:', response_fear
	print 'Joy:', response_joy
	print response