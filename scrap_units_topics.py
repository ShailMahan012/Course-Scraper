# STATUS: DONE
# scrap every single section of every single unit
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
    resp = session.get(url)
    soup = bs(resp.content, "html.parser")
    # open("test.html", "wb").write(resp.content)
    return soup, resp.content


layout = """{{% extends 'care_certificate/topic_layout.html' %}}

{{% block back_to_unit %}}
{}
{{% endblock %}}

{{% block vs_custom %}}
{}
{{% endblock %}}

{{% block content %}}
{}
{{% endblock %}}

{{% block links %}}
{}
{{% endblock %}}
"""

# Write to a file of how many units and topics are done copying
def write_status(unit, topic):
    status_file = "units/status_file.txt"
    if (unit == 1 and topic == 1):
        if os.path.isfile(status_file):
            os.remove(status_file)
            print("STATUS FILE REMOVED")
    file = open(status_file, "a")
    file.write(f"UNIT: {unit} --> TOPIC: {topic}\n")
    file.close()


# Write given HTML in given  unit and topic file
def write_HTML(unit, topic, HTML):
    unit_dir = f"units/unit_{unit}/"
    file = open(f"{unit_dir}/{topic}.html", "w")
    file.write(HTML)
    file.close()


# return list of all urls of topic of given unit
def get_topic_links(unit):
    unit_dir = f"units/unit_{unit}/"
    file = open(f"{unit_dir}topic_links.txt")
    topic_links = file.read().split("\n")[:-1]
    file.close()

    return topic_links


# This is css class which contains URL of image
def get_vc_custom_CSS(soup, RESP_content):
    RESP_content = RESP_content.decode()

    image_div = soup.find("div", {"class": "wpb_column vc_column_container vc_col-sm-6 vc_hidden-xs vc_col-has-fill"})
    if not image_div:
        return ""

    image_div = image_div.find("div")
    image_div_class = image_div["class"][1]
    # print(image_div_class)

    class_index = RESP_content.find("." + image_div_class)
    class_end_index = RESP_content.find("}", class_index) + 1
    css = RESP_content[class_index:class_end_index]

    # url_index = css.find("url") + 4
    # url_end_index = css.find(")", url_index)

    # image_url = css[url_index:url_end_index]
    # print(image_url)

    return css


# We have 15 units 1 to 15
for unit_no in range(1, 16):
    topic_links = get_topic_links(unit_no)
    # [print(i) for i in topic_links]
    
    print(f"UNIT: {unit_no}, TOTAL TOPICS: {len(topic_links)}")
    
    for ic, link in enumerate(topic_links):
        topic_no = ic+1
        soup, RESP_content = get_soup(link)

        # Back to Lesson link
        back_div = soup.find("div", {"id": "learndash_back_to_lesson"}) # this
        back_div.find("a")["href"] = f"/lms/care-certificate/unit/{unit_no}"


        # Content of course
        content = soup.find("div", {"class": "learndash_content"}) # this

        # Content Image URL
        vc_custom = get_vc_custom_CSS(soup, RESP_content) # this

        # Previous link
        prev_link = soup.find("a", {"class": "prev-link"})
        if prev_link:
            prev_link["href"] = f"/lms/care-certificate/unit/{unit_no}/topic/{topic_no-1}"

        # Next link
        next_link = soup.find("a", {"class": "next-link"}) 
        if next_link:
            next_link["href"] = f"/lms/care-certificate/unit/{unit_no}/topic/{topic_no+1}"

        # prev_next_links
        links = "" # this
        if prev_link:
            links += str(prev_link) + "\n"
        if next_link:
            links += str(next_link) + "\n"

        HTML = layout.format(back_div, vc_custom, content, links)

        write_HTML(unit_no, topic_no, HTML)
        print(f"# DONE topic --{topic_no}--")
        write_status(unit_no, topic_no)

        # exit()
        # break

    print(f"#################### DONE UNIT --{unit_no}--")
    # break # break at first iteration for testing purposes

