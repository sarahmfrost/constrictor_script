import pandas as pd
import csv

import urllib.request
import requests
from urllib.request import Request

import re #regex for excluding .gif files


import time
import os #for creating a directory
from random import randint

#path = "/Users/sairah/Desktop/reddit_images/" #create a new folder on the desktop
#os.mkdir(path)


posts = []
urls = []
comments = []
subs = []
counter = 0

targetCSV = 'redditdatal.csv'
#smallerCSV = 'hotandnew_redditdata.csv'

#'top_redditdata_968.csv'
#'controversial_redditdata.csv'
#'new_redditdata.csv'
#'hot_redditdata.csv'

# first get rid of non-ASCII characters using internationalization conversion:
#iconv -c -f utf-8 -t ascii new_redditdata.csv > out.csv



with open(targetCSV, 'r', newline='') as t1:
    reader = csv.DictReader(t1)
    for row in reader:
        url = row['A']
        filename = url.split('/')[-1]
        print(filename)

# python makeURLinCSV.py > output.txt

    # with open('output2.csv', 'w') as outFile:
    #     fieldnames = ['filename']
    #     spamwriter = csv.DictWriter(outFile, fieldnames=fieldnames)
    #     for line in outFile:
    #         spamwriter.writerow(filename)


