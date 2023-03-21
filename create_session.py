import requests
import pickle

pickle_out = open("session.pickle","wb")

URL = "https://cpdonline.co.uk/login/" 
 
payload = { 
	"username-18894": "uceeifeanacho@gmail.com", 
	"user_password-18894": "ChildofGod2022",
    "form_id": "18894"
}

payload = {'username-18894': 'uceeifeanacho@gmail.com',
	'user_password-18894': 'ChildofGod2022',
	'form_id': '18894',
	'um_request': '',
	'redirect_to': 'https://cpdonline.co.uk/my-account/',
	'_wpnonce': '356822a138',
	'_wp_http_referer': '/login/'
}

session = requests.session()
response = session.post(URL, data=payload)
print(response.status_code)

pickle.dump(session, pickle_out)
pickle_out.close()

