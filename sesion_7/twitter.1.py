# -*- coding: utf-8 -*-
# export PYTHONIOENCODING=utf-8
import tweepy

consumer_key = "c3lj0ZqXCOPGYEvzr7vVsYpHK"
consumer_secret = "1O3ajogwsogND8KluAWiYB9FIYmM7ytXZSgTmhoXz1A7bI2YqB"
access_token = "64889616-a905C5DYOhrmS3ZVZKdkaU3Gl3fS1lJbQmSLciuWZ"
access_token_secret = "lVofVI18n2rf9NyeZzaE9f75vjjw0lkkEIdpGuSUMA8Pf"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.home_timeline(2)

for tweet in tweets:
    api.retweet(tweet.id)
    print(tweet.text)

# users = api.search_users("coca-cola")

# for user in users:
#     print(user)