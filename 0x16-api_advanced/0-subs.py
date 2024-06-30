import requests

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit's about page in the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Define custom headers including a User-Agent to avoid Too Many Requests error
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        # If the response status code is 200 (OK), return the number of subscribers
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the subreddit does not exist or is invalid, return 0
            return 0
    except requests.RequestException:
        # If there is any exception (network error, etc.), return 0
        return 0

