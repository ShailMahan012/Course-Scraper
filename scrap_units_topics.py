# STATUS: incomplete
# scrap every single section of every single unit
from bs4 import BeautifulSoup as bs 
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
    open("test.html", "wb").write(resp.content)
    return soup

layout = """{{% extends 'care_certificate/topic_layout.html' %}}

{{% block back_to_unit %}}
{}
{{% endblock %}}

{{% block top_title %}}
{}
{{% endblock %}}

{{% block content %}}
{}
{{% endblock %}}

{{% block audio %}}
{}
{{% endblock %}}

{{% block links %}}
{}
{{% endblock %}}
"""

def write_status(unit, topic):
    status_file = open("units/status.txt", "a")
    status_file.write(f"UNIT: {unit} --> TOPIC: {topic}\n")
    status_file.close()

# We have 15 units 1 to 15
for unit_no in range(1, 16):
    unit_dir = f"units/unit_{unit_no}/"
    topic_links = open(f"{unit_dir}topic_links.txt").read().split("\n")[:-1]
    print(f"UNIT: {unit_no}, TOTAL TOPICS: {len(topic_links)}")
    
    for ic, link in enumerate(topic_links[:]):
        topic_no = ic+1
        soup = get_soup(link)

        # Back to Lesson link
        back_div = soup.find("div", {"id": "learndash_back_to_lesson"}) # this
        back_div.find("a")["href"] = f"/lms/care-certificate/unit/{unit_no}"
        
        # Top title
        title_div = soup.find_all("div", {"class": "wpb_wrapper"})[1]
        title = title_div.find("h1").text # this

        # Content of course
        content = soup.find("div", {"class": "vc_row wpb_row vc_inner vc_row-fluid vc_row-o-equal-height vc_row-flex"}) # this

        # Audio
        audio = soup.find("audio") # this

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

        HTML = layout.format(back_div, title, content, audio, links)

        open(f"{unit_dir}/{topic_no}.html", "w").write(HTML)
        print(f"# DONE topic --{topic_no}--")
        write_status(unit_no, topic_no)
        # break

    print(f"--------------------------- DONE UNIT --{unit_no}--")
    # break # break at first iteration for testing purposes


status_file.close()