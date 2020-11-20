class Song:
    """Class to represent  a song
        Attributes:
            title (str): The title of the song
            artist (Artist): An artist object representing the songs creator.

    """

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        # self.duration = duration


class Album:
    """ Class to represent an album, using its track list
    Attributes:
        name
        year
        artist
        tracks (List[song])
    Methods:
        add_song
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds song to the track list

        Args:
            song: A song to add,
            position: if specified, the song will be added to that position in the album
                     ,otherwise , the song will be added to the end of the list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name: The name of the artist
        albums List(Album) A list of albums by this artist
            The list includes only those albums in this collection, it
            is not an exhaustive list of artists published albums
    Methods:
        add_album: Use to add a new album to the artists albums list

    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """
        Add a new album to the list
        Args:
        album

        """
        self.albums.append(album)


def find_object(field, object_list):
    """Check object list to see if object with a name attribute equal to field, exists """
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # retrieve artist object if there is one,
                # otherwise create a new artist object and add it to the artist list
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # retrieve album object if there is one,
                # otherwise create new album object and store it in the artist collection
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # create new song object and add it to the current album collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists".format(len(artists)))
