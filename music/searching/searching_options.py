def get_all_artist(artist, all_artists):
    is_exist = False
    for check_artist in all_artists:
        if check_artist.id_number == artist.id_number:
            is_exist = True
    return is_exist


def songs_artist(artist, artist_songs):
    is_exist = False
    for check_artist in artist_songs:
        if (list(check_artist.keys())[0]) == artist.id_number:
            is_exist = True
    return is_exist


def songs_artist_is_exist(artist, album_name, artist_songs):
    count = 0
    is_exist = False
    for check_artist in artist_songs:
        if (list(check_artist.keys())[0]) == artist.id_number:
            for value in artist_songs[count][artist.id_number]:
                if value == album_name:
                    is_exist = True
            if not is_exist:
                artist_songs[count][artist.id_number].append(album_name)
        count += 1
    return artist_songs


def is_song_exist(artist, song, all_songs_artist_sorted):
    count = 0
    is_exist = False
    for check_song in all_songs_artist_sorted:
        if (list(check_song.keys())[0]) == artist.id_number:
            for value in all_songs_artist_sorted[count][artist.id_number]:
                for song_name in value:
                    if song_name == song.name:
                        is_exist = True
        count += 1
    return is_exist


def sorted_songs_artist_is_exist(artist, song, all_songs_artist_sorted):
    if not is_song_exist(artist, song, all_songs_artist_sorted):
        count = 0
        # for song in all_songs_artist_sorted:
        #     if (list(song.keys())[0]) == artist.id_number:
        #         all_songs_artist_sorted[count][artist.id_number].append(song.name)
        #         # (sorted(B, key=itemgetter(1)))
    return all_songs_artist_sorted
