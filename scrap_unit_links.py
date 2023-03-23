# STATUS: DONE
from bs4 import BeautifulSoup as bs 

def get_soup(html):
    soup = bs(html, "html.parser")
    return soup

for i in range(1, 16): # 15 units from 1 to 15
    unit = f"units/unit_{i}/"

    # open topic_links file to write all links in it
    file = open(f"{unit}topic_links.txt", "w")

    # read unit index file where link for every unit is stored
    html = open(f"{unit}index.html", "r").read()

    # get soup for unit file
    soup = get_soup(html)

    # all a tag with topic-complited class
    topic_links = soup.find_all("a", {"class": "topic-completed"})
    # get quiz link
    quiz_link = soup.select_one('.completed')["href"]

    # save every link of topic
    for i in topic_links:
        file.write(str(i['href']))
        file.write("\n")
    file.close()

    # save quiz link
    open(f"{unit}quiz_link.txt", "w").write(str(quiz_link))
