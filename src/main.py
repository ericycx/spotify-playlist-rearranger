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
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    # From my own spotify developer app "My App"
    auth = ("f56b6b57452c45838b7d6936ccfbe16e", "d01aa5dc31534bc5a09e993227e46bfc")

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

results = sp.playlist_is_following("https://open.spotify.com/playlist/3eeX2jR2g3YA66Ap9vaww2?si=6f4923b47be843f1","314c7pfi6vbxgxezsx5eeshdij7i?si=bdf5c38ffbf445b1")


