from auth import spotify

def create_sentence_playlist(sentence): 
    playlistid = create_empty_playlist()
    split_sentence = sentence.split(" ")
    for i in range(len(split_sentence)):
        add_song(playlistid, split_sentence[i])



def create_empty_playlist():
        new_playlist = spotify.user_playlist_create(user=spotify.me()['id'], name="Test Playlist", public=True, collaborative=False, description="another test")
        print('\nPlaylist was created!\n')
        return new_playlist["id"]

def add_song(playlist_id, track):
    limit = 50
    initial_results = spotify.search(q='track:' + track, type='track', limit=limit)
    found = False
    j = 0
    if len(initial_results['tracks']) > 0:
        while(not found and j < 2000):
            results = spotify.search(q='track:' + track, type='track', offset=j, limit=limit)
            top_track = None
            for i in range(len(results['tracks'])):
                try: 
                    if (results['tracks']['items'][i]['name'].lower() == track.lower()):
                        top_track = results['tracks']['items'][i]['uri']
                        found = True
                        break
                except IndexError:
                    print("nothing")
                    return None

            j+=7
            if top_track != None:
                tracks = [top_track]
                spotify.user_playlist_add_tracks(user=spotify.me()['id'], playlist_id=playlist_id, tracks=tracks, position=None)
                print('\nTrack was added!\n')
            else:
                print('\nTrack was not found :(\n')



# for app.py testing purposes
def test_string(): 
    return "String from playlist.py"

# class Playlist():
#     def __init__(self, spot):
#         self.spot = spot
#         self.user= spot.me()['id']
#         self.name = "Test Playlist"
#         self.description = "Test"

#     def create_empty_playlist(self):
#         new_playlist = spot.user_playlist_create(user=user, name=name, public=True, collaborative=False, description=description)
#         return new_playlist["id"]
#         print('\nPlaylist was created!\n')
    
#     def add_song(self, playlist_id, track):
#         results = spot.search(q='track:' + track, type='track')
#         if len(results['tracks']) > 0:
#             topTrack = results['tracks']['items'][0]['uri']
#             tracks = [topTrack]
#         spot.user_playlist_add_tracks(user=user, playlist_id=playlist_id, tracks=tracks, position=None)
#         print('\nSong was added!\n')


# def add(user, playlist_id, name):
#     results = spotify.search(q='track:' + name, type='track')
#     if len(results['tracks']) > 0:
#         topTrack = results['tracks']['items'][0]['uri']
#     tracks = [topTrack]
#     spotify.user_playlist_add_tracks(user=spotify.me()['id'], playlist_id=playlist_id, tracks=tracks, position=None)