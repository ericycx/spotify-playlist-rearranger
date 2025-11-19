import time
import shuffle
import unshuffle
import reverse
from get_spotify_client import get_spotify_client

if __name__ == "__main__":
    sp = get_spotify_client()
    playlists = sp.current_user_playlists()
    playlist_names = [plist['name'] for plist in playlists['items']]
    playlist_string = ", ".join(playlist_names)
    while True:
        playlist_name = input(f"Which playlist would you like to alter? (enter list for a list of available playlists) ")
        if playlist_name == 'list':
            print(playlist_string)
        elif playlist_name in playlist_names:
            for plist in playlists['items']:
                if plist['name'] == playlist_name:
                    uri = plist["uri"]
                    length = plist['tracks']['total']
                    break
            while True:
                print("Do not pause operations half way as you may end up with half-scrambled/unscrambled playlists, which would then need to be unscrambled again")
                action = input('Would you like to shuffle, unscramble, or reverse? (S/U/R) (help if you want more info on the operations) ')
                if action == "help":
                    print("shuffle randomly rearranges songs in your playlist, unscramble reorders your playlist from the oldest addition to the newest addition")
                    print("reverse just reverses the order of the playlist, all changes can be viewed with your playlist set to custom order, the reordering can be viewed through the spotify app,")
                    print("but sometimes it freezes when there are too many songs in the playlist, but the reordering still works even if the songs aren't moving on the app")
                    print("viewing through the spotify website kind of works if you want to see the process")
                    time.sleep(3)
                elif action.upper() in ("S", "SHUFFLE"):
                    shuffle.shuffle_helper(sp, uri, length)
                    print(f"shuffled {playlist_name}")
                    break
                elif action.upper() in ("U", "UNSCRAMBLE"):
                    print('This operation will take longer, so do not pause until the unscrambling process is completed')
                    unshuffle.unscramble_helper(sp, uri, length)
                    print(f"unscrambled {playlist_name}")
                    break
                elif action.upper() in ("R", "REVERSE"):
                    reverse.reverse_helper(sp, uri,length)
                    print(f'reversed {playlist_name}')
                    break
                else:
                    print("please enter a valid operation")
            break

        else:
            print("please enter a valid playlist")




