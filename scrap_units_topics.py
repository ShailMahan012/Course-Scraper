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
    return soup

# We have 15 units 1 to 15
for i in range(1, 16):
    unit = f"units/unit_{i}/"
    topic_links = open(f"{unit}topic_links.txt").read().split("\n")[:-1]
    print(len(topic_links))
    
    for ic, link in enumerate(topic_links):
        print(link)
        soup = get_soup(link)
        print(f"# DONE SECTION --{ic+1}--")
        break

    print(f"--------------------------- DONE UNIT --{i}--")
    break # break at first iteration for testing purposes
