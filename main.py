from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)

ycom_web_page = response.text

soup = BeautifulSoup(ycom_web_page, "html.parser")
# print(soup.title)

all_anchor_tags = soup.find_all(name="a")
article_texts = []
article_links = []
for tag in all_anchor_tags:
    texts = tag.getText()
    article_texts.append(texts)
    links = tag.get("href")
    article_links.append(links)

article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_scores)

largest_number = max(article_scores)
largest_index = article_scores.index(largest_number)
print(largest_index+1)

print(article_texts[largest_index+1])
print(article_links[largest_index+1])
print(article_scores[largest_index+1])


























# # import lxml
#
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup)
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
#
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# # company_url = soup.select_one(selector="#name")
# # print(company_url)
#
# company_url = soup.select(selector=".heading")
# print(company_url)
