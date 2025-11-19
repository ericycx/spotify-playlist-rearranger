import time
from get_spotify_client import get_spotify_client

sp = get_spotify_client()

def reverse_helper(uid: str, length: int) -> None:
    new_order = list(range(length))
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
    shuffle_name = input(f"Which playlist out of {playlist_string} would you like to reverse? ")
    if shuffle_name not in playlist_names:
        print("Please enter a valid playlist")
    else:
        for plist in playlists['items']:
            if plist['name'] == shuffle_name:
                reverse_helper(plist["uri"],plist['tracks']['total'])
                print(f"reversed {shuffle_name}")
