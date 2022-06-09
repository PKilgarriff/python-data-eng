import csv
from player.music_library import Track


class MusicCSVStorage:
    def __init__(self):
        self.tracks = []

    def open(self, path_to_csv):
        with open(path_to_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                trimmed_row = map(lambda x: x.strip(), row)
                self.tracks.append(
                    Track(*trimmed_row)
                )

    def all(self):
        return self.tracks
