import tweepy
import json
import sys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
personality_insights = PersonalityInsightsV3(version='2016-10-20', username='{username}', password='{password}')



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

status = api.user_timeline(sys.argv[1], count=25)
tweets = []
for tweet in status:
	tweets.append(tweet._json["text"])
print tweets[0]
