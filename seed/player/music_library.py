class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, music_track):
        self.tracks.append(music_track)

    def remove(self, track_index):
        try:
            self.tracks.pop(track_index)
        except:
            return False
        else:
            return True

    def all(self):
        return self.tracks
