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

targetCSV = 'controversial_redditdata.csv'
smallerCSV = 'hotandnew_redditdata.csv'

#'top_redditdata_968.csv'
#'controversial_redditdata.csv'
#'new_redditdata.csv'
#'hot_redditdata.csv'

# first get rid of non-ASCII characters using internationalization conversion:
#iconv -c -f utf-8 -t ascii new_redditdata.csv > out.csv



with open(targetCSV, 'r') as t1, open(smallerCSV, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)




