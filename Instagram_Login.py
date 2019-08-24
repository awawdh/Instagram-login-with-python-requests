#Modules we need 
from bs4 import BeautifulSoup #Bs4 extracts the error message
import json
import requests

# --

#Our urls--

BASE_URL = 'https://www.instagram.com/accounts/login/'
LOGIN_URL = BASE_URL + 'ajax/'

checkip = "https://httpbin.org/ip"
 # --

 #Our requests session object.
s=requests.session()

#And we need to update and make the headers here ..

#Note : Headers define how we send a requests and it defines who we are and our user agent.

#Do not use python requests as your user agent thats not a good idea.



s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"

s.headers['upgrade-insecure-requests'] =  '1'






def login(user,passw):
  '''Login to instagram here'''

    try:
        get=s.get(BASE_URL)

        payload = {
            'username':user,
            'password':passw}

        s.headers.update({'X-CSRFToken':s.cookies['csrftoken']})   #We need to post the csrftoken 

        post = s.post(LOGIN_URL,payload,allow_redirects=True)

    except Exception: #connection error
        return False

    else:

        try:
            if s.cookies['ds_user_id']: #So if instagram gave you the user id cookies password is correct.

                print('passw is correct.')
                return True

        except KeyError:

          print('The password you entered is incorrect.')
          return False
