# -*- coding: utf-8 -*-
"""
Created on Sat Jan 06 19:59:07 2018

@author: Stefan Aleksik
"""

import os
import json
import collections
import matplotlib.pyplot as plt

path = '.'

files_in_dir = [f for f in os.listdir(path) if f.endswith('json')]
for filenames in files_in_dir:
    file_name = os.path.splitext(filenames)[0] + '.png'
    list = []
    with open(filenames, 'r') as f:
        for i in f:
            temp = json.loads(i)
            #print len(temp['category_list'])
            if len(temp['category_list']) > 0:
                for el in temp['category_list']:
                    #print el['label']
                    #print '\n'
                    list.append(el['label'])
    
    counts = collections.Counter(list)
    plt.title(file_name)
    plt.xlabel('Pie chart of topics by the user in his/her last 200 tweets')
    plt.pie([float(v) for v in counts.values()], labels=[str(k) for k in counts],
           autopct=None)
    to_save = plt.gcf()
    #plt.draw()

    to_save.set_size_inches(15, 15)

    to_save.savefig(os.path.splitext(filenames)[0], dpi=100)
    plt.clf()