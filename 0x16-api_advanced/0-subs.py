#!/usr/bin/python3
"""How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        subscribers = requests.get(url, headers=headers,
                                   allow_redirects=False).json().get("data")
        return subscribers.get("subscribers")
    except Exception:
        return 0
