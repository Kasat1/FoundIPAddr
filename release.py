import pandas as pd
import numpy as np
import csv
import re
import os
import argparse


parser = argparse.ArgumentParser(description='Found last 100 uniq IP address')
parser.add_argument("--f")
args = parser.parse_args()
f = args.f

original = open('Vagrantfile').read()
new = re.sub('[^a-zA-Z0-9\n]', ' ', original)
open('rez.txt', 'w').write(new)

df = pd.read_csv('rez.txt', header=None, delimiter=' ')
sorted = df.sort_values(by=[2, 1, 0], ascending=False)

sorted['ips'] = sorted[3].astype(str) + "." + sorted[4].astype(str) + "." + sorted[5].astype(str) + "." + sorted[6].astype(str)


uniq = sorted['ips'].unique().tolist()

prefinal = pd.DataFrame(uniq).head(100).to_string()

open('final', 'w').write(prefinal)

f = open('final')
lines = f.readlines()[1::]
f.close
f = open('final', 'w')
for line in lines:
        f.write(line[2:])
f.close

os.remove('rez.txt')
