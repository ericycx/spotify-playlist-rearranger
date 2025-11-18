import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config
import time
import json
from dateutil import parser

client_id = config.SPOTIPY_CLIENT_ID
client_secret = config.SPOTIPY_CLIENT_SECRET
redirect_uri = config.SPOTIPY_REDIRECT_URI

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="playlist-modify-private"
))

def date_added_helper(uid: str, length: int) -> list:
    # Creates a list of lists, where each list has up to 100 tuples of the index and date_added of a song in the playlist.
    # Tuples are in the form (index, date)
    date_list = []
    offset = 0
    while length > 0:
        tracks = sp.playlist_items(
            uid,
            limit=100,
            offset=offset,
            fields="items(added_at)"
        )
        for i, item in enumerate(tracks["items"]):
            date_list.append((offset + i, item["added_at"]))
        fetched = len(tracks["items"])
        if fetched == 0:
            break
        offset += fetched
        length -= fetched
        time.sleep(3)
    return date_list

def _merge(lst1: list, lst2: list) -> list:
    index1, index2 = 0, 0
    merged = [] # [youngest -> oldest song]
    while index1 < len(lst1) and index2 < len(lst2):
        d1 = parser.isoparse(lst1[index1][1])
        d2 = parser.isoparse(lst2[index2][1])

        if d1 <= d2:  # d1 is earlier or same
            merged.append(lst2[index2]) # merge the younger one (youngest -> oldest)
            index2 += 1
        else:
            merged.append(lst1[index1])  # older one first
            index1 += 1
    if index1 < len(lst1):
        # rest of the songs in lst 1 are all older than songs
        # in lst2, but still sorted form youngest to oldest
        merged.extend(lst1[index1:])
    if index2 < len(lst2):
        merged.extend(lst2[index2:])

    return merged

def mergesort(lst:list) -> list:
    if len(lst) < 2:
        return lst[:]
    else:
        mid = len(lst) // 2
        left_sorted = mergesort(lst[:mid])
        right_sorted = mergesort(lst[mid:])

        return _merge(left_sorted,right_sorted)

def no_dates(lst:list) -> list:
    # returns a list of only the indexes from a list of tuples (index, date)
    new_lst = [lst[i][0] for i in range(len(lst))]
    return new_lst

def unscramble_helper(uid: str, length: int) -> None:
    date_list = date_added_helper(uid,length)
    unscrambled_index = no_dates(mergesort(date_list))
    positions = list(range(length))
    for orig_idx in unscrambled_index:
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
    shuffle_name = input(f"Which playlist out of {playlist_string} would you like to unscramble? ")
    if shuffle_name not in playlist_names:
        print("Please enter a valid playlist")
    else:
        for plist in playlists['items']:
            if plist['name'] == shuffle_name:
                unscramble_helper(plist["uri"],plist['tracks']['total'])
                print(f"unscrambled {shuffle_name}")
