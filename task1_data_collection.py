import requests
import json
import time
from datetime import datetime
from pathlib import Path


headers = {"User-Agent": "TrendPulse/1.0"}
hacker_news_url ='https://hacker-news.firebaseio.com/v0/topstories.json'

response = requests.get(hacker_news_url, headers=headers) #get request

if response.status_code == 200:             #check if the request was successful
    story_ids = response.json()[:500]       #storing the 500 story Ids
    #print(story_ids)
else:
    print("Failed to fetch story IDs")      #message if the request is not successful

