#!/usr/bin/python3
"""Count it!"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords
    """
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        after = data['data']['after']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word] = (
                            counts.get(word, 0) + title.count(word.lower())
                        )
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(
                    counts.items(),
                    key=lambda x: (-x[1], x[0].lower())
                )
            for word, count in sorted_counts:
                print(f"{word.lower()}: {count}")
    else:
        return
