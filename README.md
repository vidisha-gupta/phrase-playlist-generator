# Spotify Phrase Playlist Generator 
This project takes in a phrase or sentence inputted as a user and creates a Spotify playlist where the songs spell the phrase.  

# WEBSITE 
To start using our website, first open your preferred browser and go to the following URL: [https://phrase-playlist-generator.herokuapp.com](https://phrase-playlist-generator.herokuapp.com/index). If it is your first time using the website, you will see a button to login in with your Spotify account. If you have a Spotify account, click on the button to open up Spotify’s authentication pop-up, which will show you which Spotify permissions are being requested, and allow you to log in to our website with Spotify. Once you are successfully logged in, you will be redirected to the main page of our website. 

Here, you can use our phrase-to-playlist generator. Simply enter a phrase or sentence you would like to turn into a Spotify playlist into the textbox with words separated by spaces and click the green “Create a Playlist” button. After a short wait, the resulting playlist will be displayed below the button that represents the phrase or sentence you inputted as songs. One or more words may have been omitted if no valid song could be found for them. You can listen to the playlist on the website after it has appeared or listen to it on the Spotify app by finding it in your “followed” playlists under the title “Your Phrase Playlist.”

# RUNNING LOCALLY
To run locally, first, clone our repository from GitHub. Make sure you have Python 3 installed on your computer (if not, download [here](https://www.python.org/downloads/)). Then, install the following libraries by entering the following commands in your console:

​ 	[Flask](https://flask.palletsprojects.com/en/1.1.x/installation/): `pip install Flask`

​	[Spotipy](https://spotipy.readthedocs.io/en/2.16.1/#installation): `pip install spotipy --upgrade`

​	[Requests](https://requests.readthedocs.io/en/master/user/install/): `python -m pip install requests`

​	[Dotenv](https://pypi.org/project/python-dotenv/): `pip install -U python-dotenv`

Go to the Spotify developer’s site and create an app. Be sure to note your client id and client secret. 
Then, you will create a `.env` file containing your **client id, client secret, and redirect URI**. The first two can be found on the Spotify developer dashboard. Set the redirect URI to be “http://127.0.0.1:5000/callback” (or comment line 17 and uncomment line 20 in `app.py`). Be sure to whitelist this url within your app on the Spotify developer dashboard. 
> Alternatively, you can just ignore dotenv and os, and just write your secrets directly on lines 15-17 in `app.py`. Just remember that this should <u>only be done if running locally</u> as you don’t want anyone else to have access to these values. 

Finally, run the `app.py` file. Feel free to uncomment print statements for debugging purposes. If all the previous steps were done correctly, the console will display a link to a local host (http://127.0.0.1:5000/). Click on this link to run the app locally. You’re all done! To stop running, click within the console and press `CTRL + C`.
    
