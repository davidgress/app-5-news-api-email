import requests

api_key = "28d7c28066974f13b60bbbf287f3dc49"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2023-07-12&sortBy=publishedAt&apiKey=" \
    "28d7c28066974f13b60bbbf287f3dc49"

request = requests.get(url)
content = request.text
print(content)