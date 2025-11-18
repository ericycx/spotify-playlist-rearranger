import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config
import random
import json
import time

client_id = config.SPOTIPY_CLIENT_ID
client_secret = config.SPOTIPY_CLIENT_SECRET
redirect_uri = config.SPOTIPY_REDIRECT_URI

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="playlist-modify-private"
))

def shuffle_helper(uid: str, length: int) -> None:
    new_order = list(range(length))
    random.shuffle(new_order)
    positions = list(range(length))
    for orig_idx in new_order:
        current_pos = positions.index(orig_idx)
        print(f"Moving track at current_pos={current_pos}")
        sp.playlist_reorder_items(uid, range_start=current_pos, insert_before=0)
        moved = positions.pop(current_pos)
        positions.insert(0, moved)
        time.sleep(0.1)

if __name__ == "__main__":
    playlists = sp.current_user_playlists()
    playlist_names = [plist['name'] for plist in playlists['items']]
    playlist_string = ", ".join(playlist_names)
    shuffle_name = input(f"Which playlist out of {playlist_string} would you like to shuffle? ")
    if shuffle_name not in playlist_names:
        print("Please enter a valid playlist")
    else:
        for plist in playlists['items']:
            if plist['name'] == shuffle_name:
                shuffle_helper(plist["uri"],plist['tracks']['total'])
                print(f"shuffled {shuffle_name}")
