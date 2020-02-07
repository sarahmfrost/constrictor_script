#reddit_scrape_praw
#affective interaction?

import praw #Python Reddit API Wrapper
import pandas as pd
import csv

import urllib.request
import requests
from urllib.request import Request
import shutil


import time
import os #for creating a directory
from random import randint



posts = []
urls = []
comments = []
subs = []
counter = 0

with open('urlnew.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row['url']
        filename = url.split('/')[-1]
        print(filename)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)




        #urllib.request.urlretrieve(url, path + filename) #retrieve images and put them in folder
        #
        value = randint(0, 8)
        time.sleep(value) # make random
        counter+=1
        print("counter is", counter)

csvfile.close()




