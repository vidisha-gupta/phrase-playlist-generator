from flask import Flask, render_template, request
from playlist import create_playlist

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
def index():
    link = ""
    output = ""
    if request.method == 'POST':
        playlist_uri = create_playlist(request.form['phrase'])
        if not playlist_uri: 
            output = "No songs were found. Please try again."
        else:
            link = f"https://open.spotify.com/embed/playlist/{playlist_uri}"
            output = f"Your playlist was created! Some songs may be missing if they were not found."

    return render_template('index.html', output=output, link=link)

if __name__ == '__main__':
    app.run()    