# STATUS: DONE
from bs4 import BeautifulSoup as bs 

def get_soup(html):
    soup = bs(html, "html.parser")
    return soup

course_layout = "flask_app/templates/care_certificate/course_layout.html"

soup = get_soup(open(course_layout).read())

all_units = soup.find_all("ul")


for ic, unit in enumerate(all_units):
    unit_no = ic + 1
    topics = unit.find_all("a", {"class": "topic-completed"})
    
    for ix, topic_link in enumerate(topics):
        topic_no = ix + 1
        topic_link["href"] = f"/lms/care-certificate/unit/{unit_no}/topic/{topic_no}"

open(course_layout, "w").write(str(soup))

# check http://127.0.0.1:8081/lms/care-certificate/unit/8/topic/50