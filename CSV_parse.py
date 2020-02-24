import pandas as pd
import csv

import urllib.request
import requests
from urllib.request import Request

import re #regex for excluding .gif files


import time
import os #for creating a directory
from random import randint


posts = []
urls = []
comments = []
subs = []
counter = 0

targetCSV = 'redditdatal.csv'



with open(targetCSV, 'r', newline='') as t1:
    reader = csv.DictReader(t1)
    for row in reader:
        url = row['A']
        filename = url.split('/')[-1]
        print(filename)

# python makeURLinCSV.py > output.txt

