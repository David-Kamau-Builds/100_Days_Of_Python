from bs4 import BeautifulSoup

with open ("website.html") as file:
    website_content = file.read()

soup = BeautifulSoup(website_content, "html.parser")
print(soup.title.name)
print(soup.title.string + "\n")
print(soup.prettify())

all_tags = soup.find_all("a")
for tag in all_tags:
    print(tag.string + " - " + tag.get("href"))

heading = soup.find(name="h1", id="name")
section_heading = soup.find(name="h3", class_="heading")
print(heading.string + "\n ")
print(section_heading.string + "\n ")

company_url = soup.select_one(selector="p a")
company_url_link = tag.get("href" ,company_url)
print(company_url_link)