import tweepy
import json
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

status = api.user_timeline(sys.argv[1], count=25)
tweets = []

for tweet in status:
    print tweets.append(tweet._json["text"])
