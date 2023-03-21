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

for i in range(1, 16):
    unit = f"units/unit_{i}/"
    topic_links = open(f"{unit}topic_links.txt").read().split("\n")[:-1]
    print(len(topic_links))
    
    for link in topic_links:
        soup = get_soup(link)

    break # break at first iteration for testing purposes
