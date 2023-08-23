import bs4


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


with open("website.html") as f:
    content = f.read()

soup = bs4.BeautifulSoup(content, "html.parser")

all_anchor_tag = soup.find_all(name="a")
for tag in all_anchor_tag:
    print(bcolors.OKCYAN + tag.get("href") + bcolors.ENDC)

# other exemples
heading = soup.find(name="h1", id="name")
print(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

name = soup.select_one(selector="#name")
print(name)
