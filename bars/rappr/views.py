# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
	return HttpResponse("Let's analyze today's greatest rappers, and their lyrics!")
def detail(request, rapper):
	import tweepy
	import json
	import sys
	from watson_developer_cloud import PersonalityInsightsV3
	from bs4 import BeautifulSoup
	import urllib2
	from watson_developer_cloud import NaturalLanguageUnderstandingV1
	import watson_developer_cloud.natural_language_understanding.features.v1 \
	  as Features
	import sys

	consumer_key = ''
	consumer_secret = ''
	access_token = ''
	access_token_secret = ''

	personality_insights = PersonalityInsightsV3(version='2016-10-20', username='', password='')



	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)


	api = tweepy.API(auth)

	status = api.user_timeline(rapper, count=100)

	tweets = []
	for tweet in status:
		tweets.append(tweet._json["text"])
	tweeter = ' '.join(tweets)



	profile = personality_insights.profile(tweeter, content_type='text/plain', raw_scores=True, consumption_preferences=True)
	# needs = profile["needs"]
	personality = profile["personality"]

	# insight_need = []
	insight_personality = []
	raw_score_minimum = .80
	raw_score_personality = 0.60
	raw_score_trait = 0.70

	# for need in needs:
	# 	if need["raw_score"] > raw_score_minimum:
	# 		insight_need.append(str(need["name"])) 

	for personalities in personality:
		if personalities["raw_score"] > raw_score_personality:
			for personal in personalities["children"]:
				if personal["raw_score"] > raw_score_trait:
					insight_personality.append(str(personal["name"]))
	insight_personalities = ', '.join(insight_personality)
	
	return HttpResponse('The personalitry traits include: %s' % insight_personalities)

def results(request, rapper, music):
	import json
	from bs4 import BeautifulSoup
	import urllib2
	from watson_developer_cloud import NaturalLanguageUnderstandingV1
	import watson_developer_cloud.natural_language_understanding.features.v1 \
	  as Features

	

	natural_language_understanding = NaturalLanguageUnderstandingV1(username="", password="", version="")

	baseUrl = 'http://www.azlyrics.com/lyrics/{}/{}.html'.format(rapper,music)
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