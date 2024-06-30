#!/usr/bin/python3
"""Recursive function to return a list of hot post titles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 404:
            return None

        # Check if response is JSON
        try:
            results = response.json().get("data", {})
        except ValueError:
            return None

        children = results.get("children", [])
        if not children:
            return hot_list

        for c in children:
            hot_list.append(c.get("data", {}).get("title", "None"))

        after = results.get("after")
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except requests.RequestException as e:
        return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is None:
            print("None")
        else:
            print(result)

