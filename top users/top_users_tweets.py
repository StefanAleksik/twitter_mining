# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 17:36:35 2018

@author: Stefan Aleksik
"""

import pandas as pd

import tweepy
import csv

consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''

#importing the tweets from metoo
tweets = pd.read_csv('..\merge.csv', sep=';', encoding='utf-8-sig')

#converting obj to float64 for the number of tweets and retweets
tweets['retweets'] = pd.to_numeric(tweets['retweets'], errors='coerce')
tweets['favorites'] = pd.to_numeric(tweets['favorites'], errors='coerce')

sorted_tweets = tweets.sort_values(by=['retweets', 'favorites'], ascending=False)
top_100_tweets = sorted_tweets[:100]

top_100_users = top_100_tweets['username'].astype(str)
top_5_users = top_100_users[:5].tolist()

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)

	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f, delimiter=';')
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
      for user in top_5_users:
          get_all_tweets(user)