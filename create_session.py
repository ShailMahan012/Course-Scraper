from bs4 import BeautifulSoup as bs 
import requests
import pickle



def get_soup(session, url):
    resp = session.get(url)
    soup = bs(resp.content, "html.parser")
    return soup


def login(URL, wpnonce):
    print("Loging in ...")
    # Data to post on URL
    payload = {
        'username-18894': 'uceeifeanacho@gmail.com',
        'user_password-18894': 'ChildofGod2022',
        'form_id': '18894',
        'um_request': '',
        'redirect_to': 'https://cpdonline.co.uk/my-account/',
        '_wp_http_referer': '/login/'
    }
    payload["_wpnonce"] = wpnonce
    # create request session
    session = requests.session()
    # send post request
    response = session.post(URL, data=payload)
    # open("login_account.html", "wb").write(response.content)
    print(response.status_code)
    return session


def save_session(session):
    # open file as write bytes
    pickle_out = open("session.pickle", "wb")

    # save session object to pickle_out
    pickle.dump(session, pickle_out)
    pickle_out.close()
    print("Session Saved")


def get_wpnonce(URL):
    print("Getting _wpnonce ...")
    soup = get_soup(requests, URL)
    wpnonce = soup.find("input", {"id": "_wpnonce"})['value']
    print("_wpnonce: " + wpnonce)
    return wpnonce


# URL for login
URL = "https://cpdonline.co.uk/login/" 
wpnonce = get_wpnonce(URL)
session = login(URL, wpnonce)
save_session(session)



# Now sessoin has been saved. no need to login to website again and again
# Just read session file