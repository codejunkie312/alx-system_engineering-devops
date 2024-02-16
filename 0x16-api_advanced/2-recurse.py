#!/usr/bin/python3
"""hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """returns a list of hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}

    try:
        posts = requests.get(url, headers=headers, params=params,
                             allow_redirects=False).json().get("data")
        for post in posts.get("children"):
            hot_list.append(post.get("data").get("title"))
        after = posts.get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except Exception:
        return None
