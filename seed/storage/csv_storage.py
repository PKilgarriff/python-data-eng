import csv
from player.music_library import Track


class MusicCSVStorage:
    def __init__(self, path_to_csv):
        self.path_to_csv = path_to_csv
        self.tracks = []

    def open_library(self):
        with open(self.path_to_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                trimmed_row = map(lambda x: x.strip(), row)
                self.tracks.append(
                    Track(*trimmed_row)
                )

    def add(self, track_to_add):
        self.tracks.append(track_to_add)

    def save_library(self):
        # Responsible for writing self.tracks to a csv
        with open(self.path_to_csv, mode="w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for track in self.tracks:
                csv_writer.writerow(
                    [track.title, track.artist, track.file, track.track_id])

    def all(self):
        return self.tracks
