# STATUS: DONE
from bs4 import BeautifulSoup as bs 

def get_soup(html):
    soup = bs(html, "html.parser")
    return soup


def get_unit_file(unit):
    file = open(f"units/unit_{unit}/index.html")
    index_file = file.read()
    file.close()
    return index_file

def write_unit_file(unit, HTML):
    file = open(f"units/unit_{unit}/index.html", "w")
    file.write(HTML)
    file.close()


# 1 to 15 UNITS
for unit_no in range(1, 16):
    u_file = get_unit_file(unit_no)
    soup = get_soup(u_file)
    topics = soup.find_all("a", {"class": "topic-completed"})
    for i, link in enumerate(topics):
        link["href"] = f"/lms/care-certificate/unit/{unit_no}/topic/{i+1}"
    
    write_unit_file(unit_no, str(soup))


