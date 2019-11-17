# A copy of function from album.py

def make_album(artist, album, track=None, **album_info):
    """
    Build a dictionary that contains an album informations.
    """
    album_info['artist'] = artist
    album_info['album'] = album

    if track:
        album_info['track'] = track

    return album_info