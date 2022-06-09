import unittest

from player.music_library import Track
from storage.csv_storage import MusicCSVStorage


class TestMusicPlayer(unittest.TestCase):
    def test_constructs(self):
        mock_csv = "/Users/paul/Projects/Makers/bridge_week_01/phase_2/python-data-engineering-challenges/seed/storage/test_tracks.csv"
        MusicCSVStorage(mock_csv)

    def test_open_library(self):
        mock_csv = "/Users/paul/Projects/Makers/bridge_week_01/phase_2/python-data-engineering-challenges/seed/storage/test_tracks.csv"
        storage = MusicCSVStorage(mock_csv)
        storage.open_library()
        expected = [
            Track("Never Come Back", "Caribou", "ncb.mp3",
                  "0QEG3NGmWatNOIAVxudQfd"),
            Track("Light It Up - Remix", "Major Lazer", "light_it_up.mp3",
                  "6GKkIuMAiGVDPUkwVESbqC"),
            Track("Trouble's Coming", "Royal Blood", "troubles_coming.mp3",
                  "6voIJ7OWwRabSZDC77D5Hp"),
        ]
        self.assertEqual(storage.tracks, expected)

    def test_add(self):
        mock_csv = "/Users/paul/Projects/Makers/bridge_week_01/phase_2/python-data-engineering-challenges/seed/storage/test_tracks.csv"
        storage = MusicCSVStorage(mock_csv)
        added_track = Track("Inspector Norse", "Todd Terje",
                            "ins_norse.mp3", "2pucDx5Wyz9uHCou4wntHa")
        storage.open_library()
        storage.add(added_track)
        expected = [
            Track("Never Come Back", "Caribou", "ncb.mp3",
                  "0QEG3NGmWatNOIAVxudQfd"),
            Track("Light It Up - Remix", "Major Lazer", "light_it_up.mp3",
                  "6GKkIuMAiGVDPUkwVESbqC"),
            Track("Trouble's Coming", "Royal Blood", "troubles_coming.mp3",
                  "6voIJ7OWwRabSZDC77D5Hp"),
            Track("Inspector Norse", "Todd Terje",
                  "ins_norse.mp3", "2pucDx5Wyz9uHCou4wntHa")
        ]
        self.assertEqual(storage.tracks, expected)

    def test_add(self):
        mock_csv = "/Users/paul/Projects/Makers/bridge_week_01/phase_2/python-data-engineering-challenges/seed/storage/test_tracks.csv"
        storage = MusicCSVStorage(mock_csv)
        added_track = Track("Inspector Norse", "Todd Terje",
                            "ins_norse.mp3", "2pucDx5Wyz9uHCou4wntHa")
        storage.open_library()
        storage.add(added_track)
        expected = [
            Track("Never Come Back", "Caribou", "ncb.mp3",
                  "0QEG3NGmWatNOIAVxudQfd"),
            Track("Light It Up - Remix", "Major Lazer", "light_it_up.mp3",
                  "6GKkIuMAiGVDPUkwVESbqC"),
            Track("Trouble's Coming", "Royal Blood", "troubles_coming.mp3",
                  "6voIJ7OWwRabSZDC77D5Hp"),
            Track("Inspector Norse", "Todd Terje",
                  "ins_norse.mp3", "2pucDx5Wyz9uHCou4wntHa")
        ]
        self.assertEqual(storage.tracks, expected)

    def test_save_library(self):
        # create a music library pointing to another test file
        mock_csv = "/Users/paul/Projects/Makers/bridge_week_01/phase_2/python-data-engineering-challenges/seed/storage/test_writing_tracks.csv"
        storage = MusicCSVStorage(mock_csv)
        added_track = Track("Inspector Norse", "Todd Terje",
                            "ins_norse.mp3", "2pucDx5Wyz9uHCou4wntHa")
        storage.add(added_track)
        storage.save_library()
        pass


# file_path agnostic
# file_type csv
# import the CSV stuff
# return an array of items
