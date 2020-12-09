# This file contains functions that interact with the Spotify API for non-authentication actions
# such as creating a playlist and searching for songs

import time
start_time = time.time()

def create_playlist(sentence, spotify):
    """Creates the phrase playlist.

    Args:
        sentence (str): the phrase that will be turned into a playlist. 

    Returns:
        the ID of the generated phrase playlist.
    """ 
    if not sentence: 
        return None
    else:
        sentence = sentence[:100] # just in case the user decided to inspect element to bypass character limit
    
    tokens = sentence.split(' ')
    songs = []

    # remove null results
    for token in tokens: 
        if token_to_song(token, spotify) is not None: 
            songs.append(token_to_song(token, spotify))

    # no songs were found
    if not songs: 
        return None
    
    # if songs is not empty, create a playlist and add the songs array to the playlist
    playlist = spotify.user_playlist_create(user=spotify.me()['id'], name='Your Phrase Playlist', public=True, collaborative=False, 
                                            description='Created using the Spotify Phrase Playlist Generator: https://phrase-playlist-generator.herokuapp.com.')
    spotify.user_playlist_add_tracks(user=spotify.me()['id'], playlist_id=playlist['id'], tracks=songs, position=None)
    
    print(f"Program took {time.time() - start_time} seconds")
    
    return playlist['id']
        

def token_to_song(token, spotify):
    """Finds a song whose title is the token, ignoring case. 

    Args:
        token (str): the word to be found.

    Returns:
        str: the track URI if the song was found
        None: if the song was not found by checking the maximum amount of songs spotify allows 
              OR if there were no results to start with. 
    """
    if token in ['a', 'to', 'the']: 
        print(f'Song: \'{token}\' was excluded from the search because it is a known non-existent song.')
        return None

    if token.lower() == 'and':
        return '5cIZoKmBiFgjabaBG0D9fO'

    banned = []
    MAX_QUERY_LENGTH = 1000 # Spotify's limit
    BUFFER = 50
    banned_suffix = ""
    query = f"q='track:'{token}{banned_suffix}"

    for offset in range(0, 1000, 7):
        if len(banned) != 0:
            banned_suffix = " NOT " + " NOT ".join(word for word in banned)
        left = MAX_QUERY_LENGTH - len(query) - len("&limit=10&offset=50&type=track") - len("https://api.spotify.com/v1/search?") - BUFFER 
        # print(f"q=track:{token}{banned_suffix}")
        tracks = spotify.search(q='track:' + token + banned_suffix, type='track', limit=50, offset=offset)['tracks']['items']
        # print(f'number of results: {len(tracks)}')
        if not tracks:
            # print(f'No songs were found for the search term {token}.')
            return None
        for track in tracks:
            if track['name'].lower() == token.lower():
                # print(f'Song \'{track["name"]}\' was found with an offset of {offset}!')
                return track['uri']
            else:
                # reduce future search results by adding all words that wer e common the initial result to the banned list
                words = track['name'].split(' ')
                for word in words: 
                    if word.lower() != token.lower() and len(banned) < 20: 
                        banned.append(word)
                offset = 0
    # print(f'Song: \'{token}\' exhausted offset.')
    return None