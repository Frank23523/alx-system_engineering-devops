#!/usr/bin/python3
"""Top Ten"""

import requests
from sys import argv


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        print(post['data']['title'])


if __name__ == "__main__":
    top_ten(argv[1])
