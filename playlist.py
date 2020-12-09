# This file contains functions that interact with the Spotify API for non-authentication actions
# such as creating a playlist and searching for songs

def create_playlist(sentence, spotify):
    """Creates the phrase playlist.

    Args:
        sentence (str): the phrase that will be turned into a playlist. 
        spotify (Spotify Client API object): the Spotify client object. 

    Returns:
        str: the ID of the generated phrase playlist.
        None: if inputs were not valid or none of the input could be translated into song
    """ 

    # if there is no input
    if not sentence: 
        return None
    else:
         # truncate to first 100 characters just in case the user decided to inspect element to bypass character limit
        sentence = sentence[:100]
    
    tokens = sentence.split(' ')
    songs = []

    # remove null results 
    for token in tokens: 
        if token_to_song(token, spotify) is not None: 
            songs.append(token_to_song(token, spotify))

    # no songs were found
    if not songs: 
        return None
    
    # if songs is not empty, create a playlist
    playlist = spotify.user_playlist_create(user=spotify.me()['id'], name='Your Phrase Playlist', public=True, collaborative=False, 
                                            description='Created using the Spotify Phrase Playlist Generator: https://phrase-playlist-generator.herokuapp.com.')
    # add the songs to the playlist
    spotify.user_playlist_add_tracks(user=spotify.me()['id'], playlist_id=playlist['id'], tracks=songs, position=None)
        
    return playlist['id']
        

def token_to_song(token, spotify):
    """Finds a song whose title is the token, ignoring case. 

    Args:
        token (str): the word to be found.
        spotify (Spotify Client API object): the Spotify client object. 

    Returns:
        str: the track URI if the song was found
        None: if the song was not found by checking the maximum amount of songs spotify allows 
              OR if there were no results to start with. 
    """
    
    # excluding common terms that do not have song equivalents 
    if token in ['a', 'to', 'the']: 
        print(f'Song: \'{token}\' was excluded from the search because it is a known non-existent song.')
        return None

    # hard-coded "and" because it is a common phrase that is difficult to find by Spotify search
    if token.lower() == 'and':
        return '5cIZoKmBiFgjabaBG0D9fO'


    banned = [] # words to exclude from search
    MAX_QUERY_LENGTH = 1000 # Spotify's limit
    banned_suffix = "" # the suffix that will be added to the search query
    query = f"q='track:'{token}{banned_suffix}" 

    # go through 1000 offsets and find a matching song
    for offset in range(0, 1000, 7):
        if len(banned) != 0:
            banned_suffix = " NOT " + " NOT ".join(word for word in banned)
        # print(f"q=track:{token}{banned_suffix}")
        # the search results, excluding banned terms
        tracks = spotify.search(q='track:' + token + banned_suffix, type='track', limit=50, offset=offset)['tracks']['items']
        
        # no tracks were found
        if not tracks:
            # print(f'No songs were found for the search term {token}.')
            return None
        
        # check all tracks in results for a match
        for track in tracks:
            if track['name'].lower() == token.lower():
                # print(f'Song \'{track["name"]}\' was found with an offset of {offset}!')
                return track['uri']
            else:
                # reduces future search results by adding all "extra" words to a banned list
                words = track['name'].split(' ')
                for word in words: 
                    # makes sure to not add too many to banned list so that query is within Spotify's character limit
                    if word.lower() != token.lower() and len(banned) < 20: 
                        banned.append(word)
                # reset offset to search with new query that excludes banned words
                offset = 0
    # print(f'Song: \'{token}\' exhausted offset.')
    # nothing was found after going through all offsets
    return None