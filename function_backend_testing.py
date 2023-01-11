import requests
from requests import RequestException
from db_connector import get_user

#A request to the backend server with a POST request to add a user to the database
#url_test (str), user_name(str)
def post_test(url_test,user_name):
    try:
        requests.post(url_test,json={"user_name":user_name})
    except RequestException:
        raise RequestException("test failed")

#A request to the backend server with a GET request to obtain information about the user from the database
#url_test (str)
def get_backend_test(url_test):
    try:
        res = requests.get(url_test)
        if res.ok:
            print(res.json())
    except RequestException:
        raise RequestException("test failed")

#The function checks that the username returned from the reference is stored in the database
#user_id(int) user_name_test(str)
def check_username_test(user_id,user_name_test):
    try:
        user_name = get_user(user_id)
        if user_name == user_name_test:
            return (True)
        return (False)
    except RequestException:
        raise RequestException("test failed")
