# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 15:13:54 2018

@author: Stefan Aleksik
"""

import requests
from time import sleep
import os
import pandas as pd
import urllib

url = "http://api.meaningcloud.com/class-1.1"

key = 'key=<YOUR KEY>&txt='
model = '&model=SocialMedia_en'

headers = {'content-type': 'application/x-www-form-urlencoded'}



path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('csv')]
for filenames in files_in_dir:
    file_name = os.path.splitext(filenames)[0] + '_classification.json'
    jsonfile = open(file_name, 'w')
    df = pd.read_csv(filenames, error_bad_lines=False, sep = ';', encoding='utf-8-sig')
    for index, row in df.iterrows():
        txt = urllib.quote_plus(row['text'].encode('utf8'))
        payload = key + txt + model
        response = requests.request("POST", url, data=payload, headers=headers)
        jsonfile.write(response.text.encode('utf8'))
        jsonfile.write('\n')
        sleep(0.5)
    jsonfile.close()
    #print df['text']    
