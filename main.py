import requests
from requests.auth import HTTPBasicAuth

CLIENT_ID = ...
CLIENT_SECRET = ...
USERNAME = ...
PASSWORD = ...

auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

data = {
    "grant_type": ...,
    "username": ...,
    "password": ...,
}

headers = {
    "User-Agent": ...,
}

r = requests.post(
    "https://www.reddit.com/api/v1/access_token",
    auth=auth,
    data=data,
    headers=headers,
    timeout=10,
)

...
