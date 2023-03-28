# STATUS: DONE

# Scrap Topic links and titles
# Srap Quiz links and titles
# Scrap all unit titles

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
all_units_top = side_bar.find_all("div", {"class": "lesson"})
all_units = side_bar.find_all("ul")

# Write title for every unit
unit_title_file = open(f"units/unit_titles.txt", "w")
for i in all_units_top:
    title = i.text.strip()
    unit_title_file.write(title)
    unit_title_file.write("\n")
unit_title_file.close()
    

# Write title and link of topic and quiz for every topic in specific unit_no file
for i, unit in enumerate(all_units):
    unit_path = f"units/unit_{i+1}/"
    topic_file = open(f"{unit_path}topic_links.txt", "w")
    topic_title_file = open(f"{unit_path}topic_titles.txt", "w")
    quiz_file = open(f"{unit_path}quiz_links.txt", "w")
    quiz_title_file = open(f"{unit_path}quiz_titles.txt", "w")

    li_items = unit.find_all("li", {"class": ""})
    li_quiz = unit.find_all("li", {"class": "quiz-item"})
    for li in li_items:
        link = li.find("a")
        topic_file.write(link["href"])
        topic_file.write("\n")
        topic_title_file.write(link.text)
        topic_title_file.write("\n")


    for li in li_quiz:
        link = li.find("a")
        quiz_file.write(link["href"])
        quiz_file.write("\n")
        quiz_title_file.write(link.text)
        quiz_title_file.write("\n")

    topic_file.close()
    topic_title_file.close()
    quiz_file.close()
    quiz_title_file.close()
