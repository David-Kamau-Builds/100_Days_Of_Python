from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

stories = []

for item in soup.select("tr.athing"):
    title_tag = item.select_one(".titleline a")
    title = title_tag.text
    link = title_tag["href"]

    subtext = item.find_next_sibling("tr")
    score_tag = subtext.select_one(".score")

    points = int(score_tag.text.replace(" points", "")) \
        if score_tag else 0

    stories.append({
        "title": title,
        "link": link,
        "points": points,
    })

stories.sort(key=lambda x: x["points"], reverse=True)

for story in stories:
    print(f"{story['points']:>4} | {story['title']}")
    print(f"     {story['link']}\n")