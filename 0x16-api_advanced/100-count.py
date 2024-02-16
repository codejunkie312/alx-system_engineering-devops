#!/usr/bin/python3
"""count words in subreddit"""
import requests


def count_words(subreddit, word_list, after="", word_count={}):
    """returns a list of hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}

    try:
        posts = requests.get(url, headers=headers, params=params,
                             allow_redirects=False).json().get("data")
        for post in posts.get("children"):
            title = post.get("data").get("title").lower().split()
            for word in word_list:
                word = word.lower()
                if word in title:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        after = posts.get("after")
        if after is not None:
            return count_words(subreddit, word_list, after, word_count)
        else:
            if not word_count:
                print()
            else:
                for key, value in sorted(word_count.items(),
                                         key=lambda x: (-x[1], x[0])):
                    print("{}: {}".format(key, value))
    except Exception:
        return None
