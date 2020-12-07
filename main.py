# LOCAL TESTING 
from playlist import create_playlist
from auth import runAuth

# spot = runAuth()
# results = spot.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])    

create_playlist("i love cheese")
