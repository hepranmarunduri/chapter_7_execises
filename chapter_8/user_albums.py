def make_album(artist, album, **album_info):
    """Build a dictionary that contains an album informations."""
    album_info['artist'] = artist
    album_info['album'] = album

    return album_info

while True:
    opening = input("Answer all questions. Type 'ok'."
                    "\n(or Press 'q' to quit) ")

    if opening == 'q':
        break

    elif opening == 'ok':
        print("")
        ask_artist = input("Who's your favorite artist? ")
        print("")
        prompt_ask_album = "and from all his/her albums, "
        prompt_ask_album += "Which one is your favorite? "
        ask_album = input(prompt_ask_album)
        print("")
        print("Thank You!!")
        print("")
        print(make_album(ask_artist, ask_album))
        print("\n\n")
    
    else:
        print("")
        continue