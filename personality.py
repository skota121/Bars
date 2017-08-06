import tweepy
import json
consumer_key = 'secret'
consumer_secret = 'secret'
access_token = 'secret'
access_token_secret = 'secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
