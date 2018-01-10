# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 07:50:00 2017

@author: Stefan Aleksik
"""

import pandas as pd
import matplotlib.pyplot as plt

#importing the sentiments
sentiment = pd.read_csv('sentiment.csv', names = ["sentiment"])

#import your data here

#Plot a histogram of frequencies
sentiment.sentiment.value_counts().plot(kind='barh')
plt.title('Number of appearances in dataset')
plt.xlabel('Sentiment barh chart')

to_save = plt.gcf()
plt.draw()

to_save.set_size_inches(15, 15)

to_save.savefig('sentiment_en.png', dpi=100)
print sentiment.sentiment
