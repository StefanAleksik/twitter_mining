# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 14:49:15 2018

@author: Stefan Aleksik
"""

import json
import io
#import os

txtfile = open('all_topics.txt', 'w')
very_big_string = ''

with io.open('topics.json', 'r', encoding='utf-8-sig') as f:
    for i in f:
        try:    
            json.loads(i)
        except ValueError:
            continue
        temp = json.loads(i)
        #print temp
        for el in temp['entity_list']:
            very_big_string += (el['form'].encode('utf-8') + ', ')
             
    f.close()
    txtfile.write(very_big_string)
    print very_big_string            