import requests
from send_email import send_email


topic = "tesla"
api_key = "28d7c28066974f13b60bbbf287f3dc49"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=28d7c28066974f13b60bbbf287f3dc49&" \
      "language=en"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
count = 0
for article in content["articles"][20:]:
    if count == 0:
        body = "Subject: Today's news " + "\n" + \
               body + article['title'] + "\n" + article['description'] + \
               "\n" + article['url'] + 2 * "\n"
    count += 1
    if article["title"] is not None:
        body = body + article['title'] + "\n" + article['description'] + \
               "\n" + article['url'] + 2 * "\n"
    # print(article["title"])
    # print(article["description"])
body = body.encode("utf-8")
send_email(body)
