import requests

def github_search(query: str):
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 3
    }

    response = requests.get(url, params=params)
    data = response.json()

    return [
        {
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"]
        }
        for repo in data.get("items", [])
    ]
