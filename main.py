import requests
from send_email import send_email


api_key = "28d7c28066974f13b60bbbf287f3dc49"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "sortBy=publishedAt&apiKey=" \
    "28d7c28066974f13b60bbbf287f3dc49"
# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article['title'] + "\n" + article['description'] + 2*"\n"
    # print(article["title"])
    # print(article["description"])
body = body.encode("utf-8")
send_email(body)