import spotipy, os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# access secrets
load_dotenv()
SPOTIPY_CLIENT_ID = os.environ.get("CLIENT_ID")
SPOTIPY_CLIENT_SECRET= os.environ.get("CLIENT_SECRET")
SPOTIPY_REDIRECT_URI= os.environ.get("REDIRECT_URI")

# the data we are requesting from the user
scope = "user-read-private playlist-modify-public"

def run_auth(url):
    """Runs Spotify OAuth.

    Returns:
        the Spotify API client object.
    """  
    
    o_auth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope, open_browser=False)
    o_auth.parse_response_code(url)

    print("Authentication was completed.")
    
    # send request to Spotify with user credentials, return Spotify API client object
    return spotipy.Spotify(auth_manager=o_auth)

def get_redirect_url(): 
    o_auth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope, open_browser=False)
    return o_auth.get_authorize_url()