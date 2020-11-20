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

    def get_title(self):  # getter
        return self.title
    name = property(get_title)


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
            song: A song to add, the title of a song to add
            position: if specified, the song will be added to that position in the album
                     ,otherwise , the song will be added to the end of the list
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


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

    def add_song(self, name, year, title):
        """add a new song to the collection of albums
        This method will add the song to an album in the collection.
        A new album will be created in the collection if it doesnt already exist

        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self)
            self.add_album(album_found)
        else:
            print("Found album: " + name)

        album_found.add_song(title)


def find_object(field, object_list):
    """Check object list to see if object with a name attribute equal to field, exists """
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists".format(len(artists)))
