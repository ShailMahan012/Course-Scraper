#STATUS: DONE
# read file which contains link of every unit and save main page for every unit
from bs4 import BeautifulSoup as bs 
import requests
import pickle

# read session file create by create_session.py script in which login session is stored
# no need to login to website again and again
pickle_in = open("session.pickle","rb")
session = pickle.load(pickle_in)
pickle_in.close()

def get_soup(url):
    resp = session.get(url)
    soup = bs(resp.content, "html.parser")
    return soup

# read unit links from file and split it using new line
links = open("units/unit_links.txt", "r").read().split("\n")

ic = 0
for i in links:
    print(i)
    ic += 1
    index = open(f"units/unit_{ic}/index.html", "w")
    index.write("{% extends 'care_certificate/course_layout.html' %}\n")
    index.write("{% block wpb_wrapper %}\n")
    
    soup = get_soup(i)
    wpb_wrapper = str(soup.find_all("div", {"class": "wpb_wrapper"})[0])

    course_content = str(soup.find_all("div", {"id": "learndash_lesson_topics_list"})[0])
    course_quiz = str(soup.find_all("div", {"id": "learndash_quizzes"})[0])
    bottom_links = str(soup.find_all("p", {"id": "learndash_next_prev_link"})[0])

    index.write(wpb_wrapper)
    index.write("\n{% endblock %}\n\n{% block content %}\n")
    index.write(course_content)
    index.write(course_quiz)
    index.write(bottom_links)
    index.write("\n{% endblock %}")
    print(f"DONE -- {ic}")
    
    
