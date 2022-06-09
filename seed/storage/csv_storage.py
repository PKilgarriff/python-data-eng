import csv
from player.music_library import Track


class MusicCSVStorage:
    def __init__(self):
        self.tracks = []

    def open(self, path_to_csv):
        with open(path_to_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                print(
                    f'\t{row[0]} by {row[1]} [{row[2]}/{row[3]}]')
                line_count += 1
                self.tracks.append(Track(row[0], row[1], row[2], row[3]))
            print(f'Processed {line_count} tracks.')

    def all(self):
        return self.tracks
