from dataclasses import dataclass

from storage.csv_storage import MusicCSVStorage


class MusicLibrary:
    def __init__(self, storage=MusicCSVStorage):
        self.tracks = []
        self.storage = storage
        self.import_library()

    def import_library(self):
        self.tracks = self.storage.open_library(Track)

    def export_library(self):
        self.storage.save_library(self.tracks)

    def _sort_dict(self, dict, limit=15):
        sorted_dict = {}
        sorted_keys = sorted(dict, key=dict.get, reverse=True)
        for index, key in enumerate(sorted_keys):
            if index == limit:
                break
            sorted_dict[key] = dict[key]
        return sorted_dict

    def summarise_library(self):
        summary = {}
        artists = [track.artist for track in self.tracks]
        for artist in artists:
            try:
                summary[artist]
            except:
                summary[artist] = 1
            else:
                summary[artist] += 1
        descending_summary = self._sort_dict(summary)
        return descending_summary

    def add(self, music_track):
        self.tracks.append(music_track)

    def remove(self, track_index):
        try:
            self.tracks.pop(track_index)
        except:
            return False
        return True

    def search(self, function):
        return [track for track in self.tracks if function(track)]

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
