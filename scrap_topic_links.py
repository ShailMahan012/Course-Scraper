# STATUS: DONE
from bs4 import BeautifulSoup as bs 
import pickle

pickle_in = open("session.pickle","rb")
session = pickle.load(pickle_in)
pickle_in.close()

def get_soup(url):
    resp = session.get(url)
    soup = bs(resp.content, "html.parser")
    # open("test.html", "wb").write(resp.content)
    return soup



URL = "https://cpdonline.co.uk/lms/care-certificate/"
soup = get_soup(URL)

side_bar = soup.find(class_ = "learndash_navigation_lesson_topics_list")
all_units = side_bar.find_all("ul")


for i, unit in enumerate(all_units):
    open("test.html", "w").write(str(unit))
    unit_path = f"units/unit_{i+1}/"
    topic_file = open(f"{unit_path}topic_links.txt", "w")
    quiz_file = open(f"{unit_path}quiz_links.txt", "w")

    li_items = unit.find_all("li", {"class": ""})
    li_quiz = unit.find_all("li", {"class": "quiz-item"})
    for li in li_items:
        link = li.find("a")["href"]
        topic_file.write(str(link))
        topic_file.write("\n")


    for li in li_quiz:
        link = li.find("a")["href"]
        quiz_file.write(str(link))
        quiz_file.write("\n")

    topic_file.close()
    quiz_file.close()
