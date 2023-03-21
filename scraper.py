from bs4 import BeautifulSoup as bs 
import requests 
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

s = requests.session() 
response = s.post(URL, data=payload) 
print(response.status_code) # If the request went Ok we usually get a 200 status. 

req = s.get("https://cpdonline.co.uk/lms/care-certificate/unit/care-certificate-standard-1-understanding-your-role/").content
open("test.html", "wb").write(req)

# soup = bs(response.content, "html.parser")

# protected_content = soup.find(attrs={"id": "pageName"}).text
# print(protected_content)