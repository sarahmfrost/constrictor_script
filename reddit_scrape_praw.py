#reddit_scrape_praw
#https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
#https://towardsdatascience.com/scraping-reddit-with-praw-76efc1d1e1d9
# rules: https://github.com/reddit-archive/reddit/wiki/API
# using Python 3.7.1

#https://praw.readthedocs.io/en/latest/code_overview/models/submission.html
#https://praw.readthedocs.io/en/latest/tutorials/refresh_token.html

import praw #Python Reddit API Wrapper
import pandas as pd
import csv

import urllib.request
import requests
from urllib.request import Request

import re #regex for excluding .gif files
from praw.models import MoreComments # for printing comments


import time
import os #for creating a directory
from random import randint


reddit = praw.Reddit(client_id='xxx', client_secret='xxx', password= 'xxx', redirect_uri='http://localhost:8080', user_agent='xxx', user_name='xxx')


posts = []
urls = []
comments = []
subs = []
counter = 0


art_subreddit = reddit.subreddit('Art')
for post in art_subreddit.top(limit=1000): # the limit determines the amount of results, max is 1000
    posts.append([post.url, post.id, post.title, post.score, post.num_comments])

with open('redditdata.csv', 'w', newline='') as datacsv:
    writer = csv.writer(datacsv)
    writer.writerow(["url", "ID", "title", "score", "total_comments", "shown_comments"])

    for post in posts:
        if re.findall("gif$", post[0]) or re.findall("gfycat", post[0]): #want to exclude .gif files and anything on gfycat
            continue
        if post[4] <= 20: #exclude submissions with less than 20 comments
            continue
        submission = reddit.submission(id=post[1]) # this code block downloads comments
        submission.comments.replace_more(limit=0)
        post.append(len(submission.comments)) # show amount of comments that are scraped
        for top_level_comment in submission.comments:
            if (top_level_comment.body) == "[deleted]" or (top_level_comment.body) == "[removed]":
                continue
            post.append(top_level_comment.body) # appends list of comments
        writer.writerow(post)

        counter+=1
        print(counter)
    print("done with text")


datacsv.close()




