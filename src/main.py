import spotipy
import config
from spotipy.oauth2 import SpotifyOAuth
import shuffle
import unshuffle
import reverse

client_id = config.SPOTIPY_CLIENT_ID
client_secret = config.SPOTIPY_CLIENT_SECRET
redirect_uri = config.SPOTIPY_REDIRECT_URI

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="playlist-modify-private"
))

playlists = sp.current_user_playlists()
playlist_names = [plist['name'] for plist in playlists['items']]
playlist_string = ", ".join(playlist_names)
playlist_name = input(f"Which playlist out of would you like to alter? (enter help for a list of available playlists) ")
if playlist_name == 'help':
    print(playlist_string)
elif playlist_name in playlist_names:
    for plist in playlists['items']:
        if plist['name'] == playlist_name:
            uri = plist["uri"]
            length = plist['tracks']['total']
            action = input('Would you like to shuffle, unscrambled, or reverse? (S/U/R) ')
            if action.upper() == "S" or "SHUFFLE":
                shuffle.shuffle_helper(uri, length)
                print(f"shuffled {playlist_name}")
            elif action.upper() == "U" or "UNSCRAMBLE":
                unshuffle.unscramble_helper(uri, length)
                print(f"unscrambled {playlist_name}")
            elif action.upper() == "R" or "REVERSE":
                reverse.reverse_helper(uri,length)
                print(f'reversed {playlist_name}')
            else:
                print("please enter a valid operation")
else:
    print("please enter a valid playlist")




