class Song:
    """Class to represent  a song
        Attributes:
            title (str): The title of the song
            artist (Artist): An artist object representing the songs creator.
            duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """ Class to represent an album, using its track list
    Attributes:
        title
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
            self.artist = "Various Artists"
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
