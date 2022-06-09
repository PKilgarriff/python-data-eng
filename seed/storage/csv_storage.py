import csv


class MusicCSVStorage:
    @classmethod
    def open_library(cls, output_class, csv_path="tracks.csv"):
        tracks = []
        with open(csv_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                trimmed_row = map(lambda x: x.strip(), row)
                tracks.append(
                    output_class(*trimmed_row)
                )
        return tracks

    @classmethod
    def save_library(cls, library_tracks, csv_path="tracks.csv"):
        try:
            with open(csv_path, mode="w") as csv_file:
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
