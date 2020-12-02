import spotipy, os, argparse
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# the data we are requesting from the user
scope = "user-read-private playlist-modify-public playlist-modify-private"

# access secrets from .env file
load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIPY_CLIENT_SECRET= os.getenv("CLIENT_SECRET")
SPOTIPY_REDIRECT_URI= os.getenv("REDIRECT_URI")


# send request to Spotify
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = SPOTIPY_CLIENT_ID, client_secret = SPOTIPY_CLIENT_SECRET,
                                                    redirect_uri = SPOTIPY_REDIRECT_URI, scope = scope))

def createEmptyPlaylist():
    newPlaylist = spotify.user_playlist_create(user=spotify.me()['id'], name="i loveeeee akibabi hehehhe", public=True, collaborative=False, description="test ooh ahh abolish man, return to monke")
    return newPlaylist["id"]

def add(user, playlist_id, tracks):
    print()
    spotify.user_playlist_add_tracks(user=spotify.me()['id'], playlist_id=playlist_id, tracks=tracks, position=None)

playlist = createEmptyPlaylist()

name = "baby shark"
results = spotify.search(q='track:' + name, type='track')
if len(results['tracks']) > 0:
    topTrack = results['tracks']['items'][0]['uri']

songs = [topTrack]

add(spotify.me()['id'], playlist, songs)