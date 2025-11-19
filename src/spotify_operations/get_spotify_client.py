import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=config.SPOTIPY_CLIENT_ID,
        client_secret=config.SPOTIPY_CLIENT_SECRET,
        redirect_uri=config.SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-private"
    ))
