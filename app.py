from flask import Flask, render_template, request, redirect, url_for
from playlist import create_playlist
from auth import runAuth

# create Flask app
app = Flask(__name__, template_folder='templates')

# connects index.html with python script=
# @app.route('/', methods=['POST', 'GET'])
# def index():
#     render_template('index.html')
#     spot = runAuth()
#     if spot: 
#         return render_template('main.html', output="", link="", spotify=spot)
#     return render_template('index.html')

# connects main.html with python script
@app.route('/', methods=['POST', 'GET'])
def main():
    link = ""
    output = ""
    if request.method == 'POST':
        # return request.form['phrase']
        playlist_uri = create_playlist(request.form['phrase'])
        return playlist_uri
        if not playlist_uri: 
            output = "No songs were found. Please try again."
        else:
            link = f"https://open.spotify.com/embed/playlist/{playlist_uri}"
            output = f"Your playlist was created! Some songs may be missing if they were not found."
    # displays python output in HTML 
    return render_template('main.html', output=output, link=link)

# # prevent caching issues
# @app.after_request
# def add_header(response):
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0, public'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response

# run app
if __name__ == '__main__':
    app.run(debug=True)    