#reddit_scrape_praw
#https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
#https://towardsdatascience.com/scraping-reddit-with-praw-76efc1d1e1d9
# rules: https://github.com/reddit-archive/reddit/wiki/API
# using Python 3.7.1

#https://praw.readthedocs.io/en/latest/code_overview/models/submission.html
#https://praw.readthedocs.io/en/latest/tutorials/refresh_token.html

# still to do - print all children and parents comments,
# pull url for each piece
# think about name for images stored - save it as id


#affect communication?
#how do we measure it? novelty and surprise, feasability demo
#affective interaction?

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

path = "/Users/sairah/Desktop/reddit_images/" #create a new folder on the desktop
#os.mkdir(path)


reddit = praw.Reddit(client_id='jcjXtl8eXm8Q4w', client_secret='TA7KzJkladKOwUUm5OhcCxQsc8s', password= 'Ginger0321!', redirect_uri='http://localhost:8080', user_agent='artitude', user_name='Ginger0321')
#print(reddit.user.me())
#print(reddit.auth.url(['identity'], '...', 'permanent'))
#print(reddit.auth.authorize(code))


posts = []
urls = []
comments = []
subs = []
counter = 0

#did art_subreddit.top(limit=1000)


art_subreddit = reddit.subreddit('Art')
for post in art_subreddit.gilded(limit=1000): # the limit determines the amount of results
    posts.append([post.url, post.id, post.title, post.score, post.num_comments])
    #print(post.num_comments)
    #posts = pd.DataFrame(posts,columns=['title', 'id', 'url', 'num_comments', 'body'])

with open('redditdata.csv', 'w', newline='') as datacsv:
    writer = csv.writer(datacsv)
    writer.writerow(["url", "ID", "title", "score", "total_comments", "shown_comments"])

    for post in posts:
        if re.findall("gif$", post[0]) or re.findall("gfycat", post[0]): #want to exclude .gif files and anything on gfycat ahhh
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

        #urls.append(post[0]) # This creates a list for the image urls to download
        counter+=1
        print(counter)
    print("done with text")

#urls = ["https://i.imgur.com/RFovKuM.jpg", "https://i.redd.it/5ob66o4rk81z.jpg", "https://i.redd.it/ks5qr0fe42d01.jpg","https://i.redd.it/312v3hpl41m11.jpg", "https://cdnb.artstation.com/p/assets/images/images/003/462/039/large/alena-aenami-over-the-city1k.jpg","https://gfycat.com/WhichSpanishCaimanlizard","https://gfycat.com/wigglymintyhusky","https://i.imgur.com/GRb5QS6.jpg","https://i.redd.it/ltbmuy449zj01.jpg","https://i.redd.it/aygra008zyt31.jpg"]

# for url in urls:
#     filename = url.split('/')[-1]
#     urllib.request.urlretrieve(url, path + filename) #retrieve images and put them in folder
#     #
#     value = randint(0, 8)
#     time.sleep(value) # make random
#     counter+=1
#     #print("value is", value)
#     print("counter is", counter)

datacsv.close()




