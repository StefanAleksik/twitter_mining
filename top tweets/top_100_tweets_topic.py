# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 03:18:11 2018

@author: Stefan Aleksik
"""

import pandas as pd
import urllib
import requests
from time import sleep
#import csv

url = ""
key = 'key=<YOUR KEY>&lang=en&txt='
tt = '&tt=a'
headers = {'content-type': 'application/x-www-form-urlencoded'}

tweets = pd.read_csv('..\merge.csv', sep=';', encoding='utf-8-sig', index_col=False)

#print tweets

#converting obj to float64 for the number of tweets and retweets
tweets['retweets'] = pd.to_numeric(tweets['retweets'], errors='coerce')
tweets['favorites'] = pd.to_numeric(tweets['favorites'], errors='coerce')


sorted_tweets = tweets.sort_values(by=['retweets', 'favorites'], ascending=False)
top_10000_tweets = sorted_tweets[:10000]
jsonfile = open('topics.json', 'w')
counter = 0
for index, row in top_10000_tweets.iterrows():
        counter +=1
        txt = urllib.quote_plus(row['text'].encode('utf8'))
        payload = key+txt+tt
        response = requests.request("POST", url, data=payload, headers=headers)
        print counter
        jsonfile.write(response.text.encode('utf8'))
        jsonfile.write('\n')
        sleep(0.3)
jsonfile.close
#top_100_text = top_100_tweets['text'].astype(str)