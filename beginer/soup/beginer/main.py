import bs4
import requests


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()
ycombinator_page = response.text


soup = bs4.BeautifulSoup(ycombinator_page, "html.parser")

all_title = soup.find_all(class_="titleline")
article_upvote = [ int(score.getText().split(" ")[0]) for score in soup.find_all(class_="score", name="span")]
article_title = []
article_link = []
for title in all_title:
    a_tag = title.find("a")
    title = a_tag.getText()
    article_title.append(title)
    link = a_tag.get("href")
    article_link.append(link)

result_list = []
for title, link, score in zip(article_title, article_link, article_upvote):
    entry = {"title": title, "link": link, "score": score}
    result_list.append(entry)

# Alternatively, you can achieve the same using a list comprehension
# result_list = [{"title": title, "link": link, "score": score} for title, link, score in zip(titles, links, scores)]


sorted_list = sorted(result_list, key=lambda x: x["score"], reverse=True)
# Print the resulting list of dictionaries
for entry in sorted_list:
    print(entry)