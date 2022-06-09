import os
import unittest

from player.music_library import Track
from storage.csv_storage import MusicCSVStorage


class TestMusicPlayer(unittest.TestCase):
    DIRECTORY_PATH = "/Users/paul/Projects/Makers/bridge_week_01/phase_2/python-data-engineering-challenges/seed/storage/"

    def setUp(self):
        test_writing_file = f"{self.DIRECTORY_PATH}test_writing_tracks.csv"
        file = open(test_writing_file, mode="w+")
        file.close()

    def tearDown(self):
        test_writing_file = f"{self.DIRECTORY_PATH}test_writing_tracks.csv"
        os.remove(test_writing_file)

    def test_constructs(self):
        mock_csv = f"{self.DIRECTORY_PATH}test_tracks.csv"
        MusicCSVStorage(mock_csv)

    def test_open_library(self):
        mock_csv = f"{self.DIRECTORY_PATH}test_tracks.csv"
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
        mock_csv = f"{self.DIRECTORY_PATH}test_tracks.csv"
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
        mock_csv = f"{self.DIRECTORY_PATH}test_tracks.csv"
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
        mock_csv = f"{self.DIRECTORY_PATH}test_writing_tracks.csv"
        storage = MusicCSVStorage(mock_csv)
        added_track = Track("Trouble's Coming", "Royal Blood", "troubles_coming.mp3",
                            "6voIJ7OWwRabSZDC77D5Hp")
        storage.add(added_track)
        storage.save_library()
        file = open(mock_csv)
        self.assertEqual(
            str(file.read()), "Trouble's Coming,Royal Blood,troubles_coming.mp3,6voIJ7OWwRabSZDC77D5Hp\n")


# file_path agnostic
# file_type csv
# import the CSV stuff
# return an array of items
