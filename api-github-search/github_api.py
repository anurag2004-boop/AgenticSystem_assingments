import requests

url = "https://api.github.com/search/repositories"

params = {
    "q": "python",      # search keyword
    "sort": "stars",    # sort by stars
    "order": "desc",    # descending order
    "per_page": 5       # limit to 5 results
}

response = requests.get(url, params=params)

data = response.json()

for repo in data["items"]:
    print(f"Repository: {repo['name']}")
    print(f"Stars: {repo['stargazers_count']}")
    print("-" * 30)
    