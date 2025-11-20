def get_user_playlists_list(sp) -> list:
    offset = 0
    playlists = []
    while True:
        playlist_names = [plist['name'] for plist in sp.current_user_playlists(offset = offset)['items']]
        playlists.extend(playlist_names)
        if len(playlists) != 50:
            break
        offset += 50
    return playlists

def get_minimal_playlists(sp):
    offset = 0
    playlists = []
    while True:
        page = sp.current_user_playlists(offset=offset)
        items = page["items"]
        for p in items:
            playlists.append({
                "name": p["name"],
                "uri": p["uri"],
                "track_count": p["tracks"]["total"]
            })
        if len(items) < 50:
            break
        offset += 50

    return playlists
