from bs4 import BeautifulSoup as bs 
import requests
import pickle

pickle_in = open("session.pickle","rb")
session = pickle.load(pickle_in)
pickle_in.close()

def get_soup(url):
    resp = session.get(url)
    soup = bs(resp.content, "html.parser")
    return soup

for i in range(1, 16):
    html = open(f"units/unit_{i}/index.html", "r").read()
    print(html)
