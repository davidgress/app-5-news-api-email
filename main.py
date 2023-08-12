import requests

api_key = "28d7c28066974f13b60bbbf287f3dc49"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "sortBy=publishedAt&apiKey=" \
    "28d7c28066974f13b60bbbf287f3dc49"
# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])