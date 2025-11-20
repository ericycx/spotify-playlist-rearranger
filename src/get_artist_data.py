import requests
import time
import config


client_id = config.SPOTIPY_CLIENT_ID
client_secret = config.SPOTIPY_CLIENT_SECRET
redirect_uri = config.SPOTIPY_REDIRECT_URI

TOKEN = None
TOKEN_EXPIRY = 0
off = False

def get_auth_code() -> str:
    global TOKEN, TOKEN_EXPIRY

    # If we already have a valid token, return it
    if TOKEN and time.time() < TOKEN_EXPIRY:
        return TOKEN
    url = redirect_uri
    data = {"grant_type": "client_credentials"}
    # From my own spotify developer app "My App"
    auth = (client_id, client_secret)

    response = requests.post(url, data=data, auth=auth)
    result = response.json()
    TOKEN = f"{result['token_type']} {result['access_token']}"
    TOKEN_EXPIRY = time.time() + result["expires_in"] - 60  # refresh 1 min early
    print(f"expires in: {result["expires_in"]}")
    return TOKEN

def get_artist_data(artist_URI: str) -> dict[str:object]:

    url = f"https://api.spotify.com/v1/artists/{artist_URI}"
    headers = {
        "Authorization": get_auth_code()
    }
    response = requests.get(url, headers=headers)
    return response.json()

