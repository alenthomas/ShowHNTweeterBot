from db import hn_posts_ids, write_ids
from api import get_posts, get_relevent_data
from secrets import API_KEY, API_SECRET, ACCESS_SECRET, ACCESS_TOKEN
from twython import Twython
import time

twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
tweet = """{}
{}
#ShowHN
#RetweetFromBot"""

urls = ["https://news.ycombinator.com/show",
       "https://news.ycombinator.com/show?p=2"]

def tw_format(data):
    if data["title"] and data["url"].startswith('http'):
        tweet.format(data["title"], data["url"])
        return tweet

def tweet_now(data):
    data = tw_format(data)
    twitter.update_status(status=data)

try:
    while True:
        posts = get_posts(urls)
        data = get_relevent_data(posts)
        for i in data:
            print(i["pid"])
            if i["pid"] not in hn_posts_ids:
                tweet_now(i)
                hn_posts_ids.append(i["pid"])
        time.sleep(1800)
except KeyboardInterrupt:
    print("interrupt")
    write_ids(hn_posts_ids)
