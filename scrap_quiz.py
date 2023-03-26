# STATUS: INCOMPLETE
# scrap every quiz file of every unit

from bs4 import BeautifulSoup as bs
import os
import requests
import pickle

# read session file create by create_session.py script in which login session is stored
# no need to login to website again and again
pickle_in = open("session.pickle","rb")
session = pickle.load(pickle_in) # requests session
pickle_in.close()


def get_soup(url):
    # resp = session.get(url)
    # content = resp.content
    content = open("test.html", "rb").read()
    soup = bs(content, "html.parser")
    # open("test.html", "wb").write(content)
    return soup, content


def write_HTML(HTML, unit_no):
    # file = open(f"units/unit_{unit_no}/quiz.html", "w")
    file = open(f"flask_app/templates/care_certificate/quiz_example.html", "w")
    file.write(HTML)
    file.close()


def get_quiz(soup):
    quiz = soup.find("ol", {"class": "wpProQuiz_list"})
    for li in quiz.find_all("li", recursive=False):
        del li["style"]
        li.find("div", {"class": "wpProQuiz_question_page"}).extract()
        li.find("h5", {"class": "wpProQuiz_header"}).extract()
    # exit()
    return quiz.prettify()


layout = """
<link rel="stylesheet" href="/static/quiz.css">
{{% extends 'care_certificate/quiz_layout.html' %}}

{{% block top_box %}}
{}
{{% endblock %}}

{{% block audio %}}
{}
{{% endblock %}}

{{% block quiz %}}
{}
{{% endblock %}}
"""

for unit_no in range(1, 16):
    unit_dir = f"units/unit_{unit_no}"
    url = open(f"{unit_dir}/quiz_links.txt").readline()[:-1]

    soup, content = get_soup(url)

    top_box = soup.find("div", {"class": "wpb_column vc_column_container vc_col-sm-12"}) # this

    # print(top_box)
    audio = soup.find("div", {"id": "skin_default"}) # this

    # print(audio)
    quiz = get_quiz(soup) # this
    # print(quiz)

    HTML = layout.format(str(top_box), str(audio), str(quiz))
    write_HTML(HTML, unit_no)

    print(f"DONE: {unit_no}")
    break

