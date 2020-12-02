def createEmptyPlaylist():
    spotify.user_playlist_create(user=spotify.me()['id'], name="i loveeeee akibabi hehehhe", public=True, collaborative=False, description="test ooh ahh abolish man, return to monke")

def add(user, playlist_id, name):
    results = spotify.search(q='track:' + name, type='track')
    if len(results['tracks']) > 0:
        topTrack = results['tracks']['items'][0]['uri']
    tracks = [topTrack]
    spotify.user_playlist_add_tracks(user=spotify.me()['id'], playlist_id=playlist_id, tracks=tracks, position=None)