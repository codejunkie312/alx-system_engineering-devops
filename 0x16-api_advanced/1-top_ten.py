#!/usr/bin/python3
"""Top Ten"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    try:
        posts = requests.get(url, headers=headers, params=params,
                             allow_redirects=False).json().get("data")
        for post in posts.get("children"):
            print(post.get("data").get("title"))
    except Exception:
        print("None")
