import requests
import pickle

# open file as write bytes
pickle_out = open("session.pickle","wb")

# URL for login
URL = "https://cpdonline.co.uk/login/" 

# Data to post on URL
payload = {'username-18894': 'uceeifeanacho@gmail.com',
	'user_password-18894': 'ChildofGod2022',
	'form_id': '18894',
	'um_request': '',
	'redirect_to': 'https://cpdonline.co.uk/my-account/',
	'_wpnonce': '356822a138',
	'_wp_http_referer': '/login/'
}

# create request session
session = requests.session()
# send post request
response = session.post(URL, data=payload)
print(response.status_code)

# save session object to pickle_out
pickle.dump(session, pickle_out)
pickle_out.close()


# Now sessoin has been saved. no need to login to website again and again
# Just read session file