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
twit = ' '.join(tweets)


profile = personality_insights.profile(twit, content_type='text/plain', raw_scores=True, consumption_preferences=True)
needs = profile["needs"]

insight_need = []
insight_consume =[]

for need in needs:
	insight_need.append(str(need["name"]))

print  sys.argv[1],"'s",'main needs are:', insight_need[0],',', insight_need[1],',', insight_need[2]
