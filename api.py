import requests as req
from bs4 import BeautifulSoup as bs

# article = [{"title":"Show HN: ****", "link":"https://www.github.com"}]
"""
https://news.ycombinator.com/item?id=14807779
"""

def get_bs_data(tree, tag, attribute):
    item_list = tree.findAll(tag, attribute)
    return item_list

def get_posts(url_list):
    post_list = []
    for url in url_list:
        res = req.get(url)
        parsed = bs(res.content, "html.parser")
        bulk = get_bs_data(parsed, "tr", {"class":"athing"})
        post_list.extend(bulk)
    return post_list

def get_relevent_data(posts_list):
    articles = []
    for item in posts_list:
        pid = item["id"]
        title = ""
        url = ""
        stories = get_bs_data(item, "a", {"class":"storylink"})
        for story in stories:
            title = story.text
            url = story["href"]
        articles.append({"pid":pid, "title":title, "url":url})
    return articles
