class Song:
    """Class to represent  a song

        Attributes:
            title (str): The title of the song
            artist (Artist): An artist object representing the songs creator.
            duration (int): The duration of the song in seconds. May be zero
    """

    def __int__(self, title, artist, duration):
        """

        :param title: initializes title attribute
        :param artist:  an artist object representing songs creator
        :param duration: value for duration attribute if not specified -> zero
        """
        self.title = title
        self.artist = artist
        self.duration = duration
