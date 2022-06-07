class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, music_track):
        self.tracks.append(music_track)

    def remove(self, track_position):
        track_index = track_position - 1
        self.tracks.pop(track_index)

    def all(self):
        return self.tracks
