import json

from bs4 import BeautifulSoup
import requests
import re

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")

movies = []

for movie in soup.find_all("div", {"class": "article-title-description"}):
    title_tag = movie.select_one(".article-title-description__text h3")
    full_title = title_tag.text.strip()

    # Extract ranking number (e.g. "12" from "12) The Godfather Part II")
    rank = int(re.match(r"\d+", full_title).group())
    title = re.sub(r"^\d+\)\s*", "", full_title)

    movies.append({
        "rank": rank,
        "title": title,
    })

# Sort numerically by rank
movies.sort(key=lambda x: x["rank"])


with open('movies.json', 'w') as outfile:
    json.dump(movies, outfile, indent=4)
    print("Movies Saved.")

# with open("movies.json") as infile:
#     movies = json.load(infile)
#     print(json.dumps(movies, indent=4))

with open("movies.json") as infile:
    movies = json.load(infile)

for movie in movies:
    print(f"{movie['rank']:>3}. {movie['title']}")
