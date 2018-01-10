import csv
import glob
import os
import pandas as pd
path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('csv')]
for filenames in files_in_dir:
    df = pd.read_csv(filenames, error_bad_lines=False, sep = ';')
    df.to_csv('merge.csv', mode='a', sep = ';', index=False, encode='utf-8-sig')