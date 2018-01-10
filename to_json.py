import csv
import json

csvfile = open('merge.csv', 'r',)
jsonfile = open('sentiment\all_en.json', 'w')

fieldnames = ("username","date","retweets","favorites", "text","geo", "mentions","hashtags", "id","permalink")
reader = csv.DictReader( csvfile, fieldnames, delimiter=';')
for row in reader:
    json.dump(row, jsonfile, ensure_ascii=False)
    jsonfile.write('\n')