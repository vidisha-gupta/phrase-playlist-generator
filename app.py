from flask import Flask, render_template, request, redirect, url_for
from playlist import create_playlist
from auth import run_auth, get_redirect_url
import string
import random

# keep track of sessions
sessions = {}
# code for cookie generation: https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits/23728630#23728630
session_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(64))

# create Flask app
app = Flask(__name__, template_folder='templates')
 
# login 
@app.route('/', methods=['GET'])
def login():
    return redirect(get_redirect_url())

@app.route('/callback', methods=['GET'])
def callback():
    url = request.url
    print(url)
    # store the user information in session
    sessions[session_id] = run_auth(url)
    # while session_id not in sessions:
    #     sessions[session_id] = run_auth(url)

    return redirect('/index')

# connects index.html with python script
@app.route('/index', methods=['POST', 'GET'])
def index():
    link = ""
    output = ""
    
    if request.method == 'POST':
        playlist_uri = create_playlist(request.form['phrase'], sessions[session_id])
        if not playlist_uri: 
            output = "No songs were found. Please try again."
        else:
            link = f"https://open.spotify.com/embed/playlist/{playlist_uri}"
            output = f"Your playlist was created! Some songs may be missing if they were not found."
    
    return render_template('index.html', output=output, link=link)

# run app
if __name__ == '__main__':
    app.run(debug=True)