import tweepy
from textblob import textblob

# Step Authenticate:
#Keys are specific to you, thus I didn't share it.
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Main Variable aka the Magic. With this function, we can create tweets, delete tweets, find twitter users. But, in this case, we will search tweets.
api = tweepy.API(auth)

#Search for tweets about Trump
public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

#When printed, you will see the tweet, the polarity, and the sentiment. Polarity means how positive or negative. Sentiment is how factual the data is
