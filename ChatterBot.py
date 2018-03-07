# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "FfpVXRJNcDGT1lwco9DUykuRK"
consumer_secret = "mRb9EdLNlXAMUgzOp84pL6yGxu7SAi1G7QDH7S3A1JBuCmYZBa"
access_token = "500170090-hRWfTg7QqeIhidbIVQUkA98FMf46eWiNJGFXeLBY"
access_token_secret = "NbRJU0itAtxxXS0x5ZvL3xbE8bnPLfWpmCh7ES2qGwN5o"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE