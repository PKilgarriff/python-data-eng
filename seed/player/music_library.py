class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, music_track):
        self.tracks.append(music_track)

    def all(self):
        return self.tracks
