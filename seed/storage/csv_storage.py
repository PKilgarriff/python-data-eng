import csv
from player.music_library import Track


class MusicCSVStorage:
    def __init__(self, path_to_csv="tracks.csv"):
        self.path_to_csv = path_to_csv

    def open_library(self):
        tracks = []
        with open(self.path_to_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                trimmed_row = map(lambda x: x.strip(), row)
                tracks.append(
                    Track(*trimmed_row)
                )
        return tracks

    def save_library(self, library_tracks):
        try:
            with open(self.path_to_csv, mode="w") as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',')
                for track in library_tracks:
                    csv_writer.writerow(
                        [
                            track.title,
                            track.artist,
                            track.file,
                            track.track_id
                        ])
        except:
            return False
        else:
            return True
