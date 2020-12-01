import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read user-read-private playlist-modify-public playlist-modify-private"

load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIPY_CLIENT_SECRET= os.getenv("CLIENT_SECRET")
SPOTIPY_REDIRECT_URI= os.getenv("REDIRECT_URI")

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = SPOTIPY_CLIENT_ID, client_secret = SPOTIPY_CLIENT_SECRET,
                                                    redirect_uri = SPOTIPY_REDIRECT_URI, scope = scope))

results = spotify.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])