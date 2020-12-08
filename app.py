from flask import Flask, render_template, request, redirect, url_for, session
import spotipy, os, requests
#import spotipy.util as util
from dotenv import load_dotenv
from playlist import create_playlist

# access secrets
load_dotenv()
SPOTIPY_CLIENT_ID = os.environ.get('CLIENT_ID')
SPOTIPY_CLIENT_SECRET= os.environ.get('CLIENT_SECRET')
SPOTIPY_REDIRECT_URI= os.environ.get('REDIRECT_URI')

# USE THE FOLLOWING REDIRECT URI IF RUNNING LOCALLY INSTEAD OF THE ONE ABOVE
# SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:5000/callback'

API_BASE = 'https://accounts.spotify.com'

# the data we are requesting from the user
SCOPE = 'playlist-modify-public'

# create Flask app
app = Flask(__name__, template_folder='templates')
app.secret_key = os.environ.get('FLASK_KEY')

# authorization-code-flow Step 1. Have your application request authorization
# the user logs in and authorizes access
@app.route("/")
def login():
    auth_url = f'{API_BASE}/authorize?client_id={SPOTIPY_CLIENT_ID}&response_type=code&redirect_uri={SPOTIPY_REDIRECT_URI}&scope={SCOPE}'
    print(auth_url)
    return redirect(auth_url)

# authorization-code-flow Step 2.
# Have your application request refresh and access tokens
# Spotify returns access and refresh tokens
@app.route("/callback")
def api_callback():
    session.clear()
    code = request.args.get('code')

    auth_token_url = f"{API_BASE}/api/token"
    res = requests.post(auth_token_url, data={
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":SPOTIPY_REDIRECT_URI,
        "client_id":SPOTIPY_CLIENT_ID,
        "client_secret":SPOTIPY_CLIENT_SECRET,
        })

    res_body = res.json()
    # print(res.json())
    session["toke"] = res_body.get("access_token")

    return redirect("index")

# authorization-code-flow Step 3.
# Use the access token to access the Spotify Web API;
# Spotify returns requested data
@app.route('/index', methods=['POST', 'GET'])
def index():
    link = ""
    output = ""
    
    if request.method == 'POST':
        sp = spotipy.Spotify(auth=session['toke'])
        playlist_uri = create_playlist(request.form['phrase'], sp)

        if not playlist_uri: 
            output = "No songs were found. Please try again."
        else:
            link = f"https://open.spotify.com/embed/playlist/{playlist_uri}"
            output = f"Your playlist was created! Some songs may be missing if they were not found."
    
    return render_template('index.html', output=output, link=link)

# run app
if __name__ == '__main__':
    app.run()


# # keep track of sessions
# sessions = {}
# # code for cookie generation: https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits/23728630#23728630
# session_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(64))

# @app.route('/callback', methods=['GET'])
# def callback():
#     url = request.url
#     print(url)
#     # store the user information in session
#     sessions[session_id] = run_auth(url)
#     # while session_id not in sessions:
#     #     sessions[session_id] = run_auth(url)

#     return redirect('/index')

# # login 
# @app.route('/', methods=['GET'])
# def login():
#     return redirect(get_redirect_url())