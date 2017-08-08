import tweepy
import json
import sys
from watson_developer_cloud import PersonalityInsightsV3

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

personality_insights = PersonalityInsightsV3(version='2016-10-20', username='', password='')



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

status = api.user_timeline(sys.argv[1], count=100)

tweets = []
for tweet in status:
	tweets.append(tweet._json["text"])
tweeter = ' '.join(tweets)



profile = personality_insights.profile(twit, content_type='text/plain', raw_scores=True, consumption_preferences=True)
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
print insight_personality