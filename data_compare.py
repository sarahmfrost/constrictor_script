import pandas as pd
import csv

import urllib.request
import requests
from urllib.request import Request


targetCSV = 'controversial_redditdata.csv'
smallerCSV = 'hotandnew_redditdata.csv'


with open(targetCSV, 'r') as t1, open(smallerCSV, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)




