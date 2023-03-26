# STATUS: INCOMPLETE
# scrap every quiz file of every unit

from bs4 import BeautifulSoup as bs
import copy
# import os
# import requests
# import pickle

# read session file create by create_session.py script in which login session is stored
# no need to login to website again and again
# pickle_in = open("session.pickle","rb")
# session = pickle.load(pickle_in) # requests session
# pickle_in.close()


def get_soup(content):
    soup = bs(content, "html.parser")
    return soup


def write_HTML(HTML, unit_no):
    # file = open(f"units/unit_{unit_no}/quiz.html", "w")
    file = open(f"flask_app/templates/care_certificate/quiz_example.html", "w")
    file.write(HTML)
    file.close()


def get_quiz(soup):
    all_quiz_ol = soup.find("ol", {"class": "wpProQuiz_list"})
    all_quiz = all_quiz_ol.find_all("li", recursive=False)

    one_quiz_copy = copy.copy(all_quiz[0])

    for i, one_quiz in enumerate(all_quiz):
        quiz_no = i + 1
        one_quiz.find("h5", {"class": "wpProQuiz_header"}).extract()
        one_quiz.find("div", {"class", "wpProQuiz_correct"})["style"] = "display: none;"
        one_quiz.find("div", {"class", "wpProQuiz_incorrect"})["style"] = "display: none;"
        one_quiz.find("div", {"class", "wpProQuiz_response"})["style"] = "display: none;"
        del one_quiz["data-question-meta"]
        del one_quiz["data-type"]
        del one_quiz["style"]
        del one_quiz.find("div", {"class": "wpProQuiz_question_page"})["style"]

        inputs = one_quiz.find_all("input", {"type": "radio"}) # 4 quiz options input
        for input in inputs:
            del input["disabled"]
            del input["checked"]
            input["value"] = "0" # Set every radio button value to 0

        for btn in one_quiz.find_all("input", {"type": "button"}):
            break
            btn.extract()
        # Find the correct quiz using specific CSS class
        correct = one_quiz.find("li", {"class": "wpProQuiz_questionListItem wpProQuiz_answerCorrectIncomplete"})
        if not correct:
            correct = one_quiz.find("li", {"class": "wpProQuiz_questionListItem wpProQuiz_answerCorrect"})

        correct.find("input")["value"] = "1"
        wrong = one_quiz.find("li", {"class": "wpProQuiz_questionListItem wpProQuiz_answerIncorrect"})
        if wrong:
            wrong["class"] = "wpProQuiz_questionListItem"
        correct["class"] = "wpProQuiz_questionListItem"
    

    [i.extract() for i in one_quiz_copy.find_all("div")[:-1]]
    del one_quiz_copy["data-question-meta"]
    del one_quiz_copy["data-type"]
    del one_quiz_copy["style"]
    one_quiz_copy.find("h5", {"class": "wpProQuiz_header"}).extract()
    one_quiz_copy.find("input", {"name": "back"}).extract()
    one_quiz_copy.find("input", {"name": "next"}).extract()

    btn_check = one_quiz_copy.find("input", {"name": "check"})
    btn_check["id"] = "btn_check"
    btn_check["style"] = btn_check["style"].replace("display: none;", "")
    all_quiz_ol.append(one_quiz_copy)
    return all_quiz_ol.prettify()


def get_result(soup):
    result_div = soup.find("div", {"class": "wpProQuiz_results"})

    result_div.find("p", {"class": "wpProQuiz_time_limit_expired"}).extract()
    result_div.find("p", {"class": "wpProQuiz_certificate"}).extract()
    result_div.find("div", {"class": "quiz_continue_link"}).extract()
    result_div.find("input", {"name": "reShowQuestion"}).extract()

    result_div["id"] = "result_div"
    result_div["style"] = "display: none;"
    result_div.find("input", {"name": "restartQuiz"})["id"] = "restart_quiz"
    result_div.find("span", {"class": "wpProQuiz_correct_answer"})["id"] = "correct_answers"

    result_msg = result_div.find_all("li")
    for li in result_msg:
        li["style"] = "display: none;"
    
    result_msg[0]["id"] = "msg_failed"
    result_msg[1]["id"] = "msg_passed"
    
    for scrpt in result_div.find_all("script"):
        scrpt.extract()
    return result_div.prettify()


layout = """
<link rel="stylesheet" href="/static/quiz.css">
{{% extends 'care_certificate/quiz_layout.html' %}}

{{% block top_box %}}
{}
{{% endblock %}}

{{% block audio %}}
{}
{{% endblock %}}

{{% block result %}}
{}
{{% endblock %}}

{{% block quiz %}}
{}
{{% endblock %}}
"""

for unit_no in range(1, 16):
    unit_dir = f"units/unit_{unit_no}"
    HTML = open(f"{unit_dir}/solved.html").read() # read solved quiz HTML file

    soup = get_soup(HTML)

    top_box = soup.find("div", {"class": "wpb_column vc_column_container vc_col-sm-12"}) # this

    audio = soup.find("div", {"id": "skin_default"}) # this

    result_div = get_result(soup)

    quiz = get_quiz(soup)

    HTML = layout.format(str(top_box), str(audio), str(result_div), str(quiz))
    write_HTML(HTML, unit_no)

    print(f"DONE: {unit_no}")
    break
