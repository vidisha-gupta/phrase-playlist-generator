# This file contains functions that interact with the Spotify API for non-authentication actions
# such as creating a playlist and searching for songs

import time
start_time = time.time()

def create_playlist(sentence, spotify):
    """Creates the phrase playlist.

    Args:
        sentence (str): the phrase that will be turned into a playlist. 

    Returns:
        the uri of the generated phrase playlist.
    """ 
    if not sentence: 
        return None
    
    tokens = sentence.split(' ')

    # removes null results from songs list by checking whether token_to_song(token) would return None
    # songs = list(filter(None, map(token_to_song, tokens, spotify)))
    songs = []

    for token in tokens: 
        if token_to_song(token, spotify) is not None: 
            songs.append(token_to_song(token, spotify))

    # if songs is not empty, create a playlist and add the songs array to the playlist
    if songs:
        # create an empty playlist
        playlist = spotify.user_playlist_create(user=spotify.me()['id'], name="Your Phrase Playlist", public=True, collaborative=False, 
                                                description="Created using the Spotify Phrase Playlist Generator: https://github.com/vidisha-gupta/phrase-playlist-generator.")
        # add songs list to the playlist
        spotify.user_playlist_add_tracks(user=spotify.me()['id'], playlist_id=playlist['id'], tracks=songs, position=None)
        
        print(f"Program took {time.time() - start_time} seconds")
        
        return playlist['uri'].replace("spotify:playlist:", "")
        

def token_to_song(token, spotify):
    """Finds a song whose title is the token, ignoring case. 

    Args:
        token (str): the word to be found.

    Returns:
        str: the track URI if the song was found
        None: if the song was not found by checking the maximum amount of songs spotify allows 
              OR if there were no results to start with. 
    """
    # CAN IMPLEMENT BAN CHECK IF TIME
    # banned = ['love', 'loves', 'all', '2', 'alone', 'he', 'heart', 'never', 'boys', 'la', 'come', '3', 'but', 'up', 'little', 'that', 'one', 'fall', 'baby', 'we', 'were', 'you', 'the', 'say', 'summer', 'mind', 'this', 'eyes', 'hell', 'and', 'new', 'an', 'stay', 'have', 'his', 'had', 'see', 'from', 'ya', 'hey',  'miss', 'song', 'hers', 'her', 'it', 'girl', 'they', 'sad', 'to', 'feat.', 'me', 'im', 'she', 'go', 'happy', 'as', 'don\'t', 'can\'t', 'won\'t', 'u', 'been', 'time', 'are', 'what', 'better', 'keep', 'word', 'a', 'like', 'can', 'when', 'do', 'of', 'my', 'always', 'fuck', 'is', 'good', 'boy', 'dance', 'for', 'life', 'something', 'die', 'I', 'with', 'was', 'worse', 'not', 'cant', 'in', 'said', 'mine', 'at', 'or', 'someone', 'your', 'break', 'goodbye', '1', 'girls', 'yeah', 'ft.', 'by', 'money', 'wake', 'be', 'somewhere', 'yours', 'crush', 'on']
    # banned = ['love'] 
    # ban_suffix = " " + " NOT ".join(word for word in banned if word not in token.lower())
    # print(token)
    # print(ban_suffix)
    for offset in range(0, 2000, 10):
        tracks = spotify.search(q='track:' + token, type='track', offset=offset)['tracks']['items']
        # print(f'number of results: {len(tracks)}')
        if not tracks:
            print(f"No songs were found for the search term {token}.")
            return None
        for track in tracks:
            if track['name'].lower() == token.lower():
                print(f'Song: {track["name"]} was found with an offset of {offset}!')
                return track['uri']
    print(f"Song: {token} exhausted offset.")
    return None