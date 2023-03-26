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
    resp = session.get(url)
    soup = bs(resp.content, "html.parser")
    open("test.html", "wb").write(resp.content)
    return soup, resp.content

for unit_no in range(1, 16):
    unit_dir = f"units/unit_{unit_no}"
    url = open(f"{unit_dir}/quiz_links.txt").readline()[:-1]

    soup = get_soup(url)
    print(f"DONE: {unit_no}")
    break