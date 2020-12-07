import spotipy, os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

def runAuth():
    """Runs Spotify OAuth.

    Returns:
        the Spotify API client object.
    """  
    # the data we are requesting from the user
    scope = "user-read-private playlist-modify-public"

    # access secrets
    load_dotenv()
    SPOTIPY_CLIENT_ID = os.environ.get("CLIENT_ID")
    SPOTIPY_CLIENT_SECRET= os.environ.get("CLIENT_SECRET")
    SPOTIPY_REDIRECT_URI= os.environ.get("REDIRECT_URI")

    # send request to Spotify with user credentials, return Spotify API client object
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope))
    # TESTING VERSION
    #spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri='http://127.0.0.1:5000/', scope=scope))
    
    print("Authentication was completed.")

    return spotify