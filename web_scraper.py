import requests
import string
import os
from bs4 import BeautifulSoup

number_of_pages = int(input())
article_type_usr = input()
owd = os.getcwd()
for i in range(1, number_of_pages + 1):
    os.mkdir(f"Page_{str(i)}")
    page_url = "https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page=" + \
               str(i)
    soup = BeautifulSoup(requests.get(page_url).content, 'html.parser')
    article_title = soup.find_all("a", {"data-track-action": "view article"})
    article_type = soup.find_all("span", {"data-test": "article.type"})
    for x in range(len(article_type)):
        if article_type[x].text == "\n" + article_type_usr + "\n":
            article = article_title[x].text.translate(str.maketrans('', '', string.punctuation)).replace(" ", "_") + \
                      ".txt"
            os.chdir(f"Page_{i}")
            article_url = "https://www.nature.com" + article_title[x]["href"]
            article_soup = BeautifulSoup(requests.get(article_url).content, "html.parser")
            article_body = article_soup.find("div", "c-article-body main-content").text
            file = open(article, "wb")
            file.write(bytes(article_body.encode("utf-8")))
            file.close()
            os.chdir(owd)
print("Saved all articles.")
