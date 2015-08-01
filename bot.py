_author__ = 'amalhotra'
import tweepy
import time
import sys

ReadFile = (sys.argv[1])
CONSUMER_KEY = 'Key goes here'
CONSUMER_SECRET = 'Key goes here'
ACCESS_KEY = 'Key goes here'
ACCESS_SECRET = 'Key goes here'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

with open(ReadFile) as file:
    tweets=file.read().splitlines()
    file.close()

#read each tweet
for tweet in file:
    api.update_status(status=tweets)
# every 30 mins
    time.sleep(1800)