def make_album(artist, album, track=None, **album_info):
    """Build a dictionary that contains an album informations."""
    album_info['artist'] = artist
    album_info['album'] = album

    if track:
        album_info['track'] = track

    return album_info


print(make_album('a7x', 'avenged sevenfold'))
print(make_album('peterpan', 'hari yang cerah'))
print(make_album('lee hi', '24 degree celcius', 5))