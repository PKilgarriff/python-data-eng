from dataclasses import dataclass


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

    def search(self, function):
        return list(filter(function, self.tracks))

    def all(self):
        return self.tracks


@dataclass
class Track:
    title: str
    artist: str
    file: str
    track_id: str = "4uLU6hMCjMI75M1A2tKUQC"

    def __str__(self):
        return f"{self.title} by {self.artist}"

    def link(self):
        return str(f"https://open.spotify.com/track/{self.track_id}")
