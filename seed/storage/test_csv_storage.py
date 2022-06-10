import os
import unittest

from player.music_library import Track
from storage.csv_storage import MusicCSVStorage


class TestMusicCSVStorage(unittest.TestCase):
    DIRECTORY_PATH = "/Users/paul/Projects/Makers/bridge_week_01/phase_2/python-data-engineering-challenges/seed/storage/"

    def setUp(self):
        test_writing_file = f"{self.DIRECTORY_PATH}test_writing_tracks.csv"
        file = open(test_writing_file, mode="w+")
        file.close()

    def tearDown(self):
        test_writing_file = f"{self.DIRECTORY_PATH}test_writing_tracks.csv"
        os.remove(test_writing_file)

    def test_open_library(self):
        mock_csv = f"{self.DIRECTORY_PATH}test_tracks.csv"
        expected = [
            Track("Never Come Back", "Caribou", "ncb.mp3",
                  "0QEG3NGmWatNOIAVxudQfd"),
            Track("Light It Up - Remix", "Major Lazer", "light_it_up.mp3",
                  "6GKkIuMAiGVDPUkwVESbqC"),
            Track("Trouble's Coming", "Royal Blood", "troubles_coming.mp3",
                  "6voIJ7OWwRabSZDC77D5Hp"),
        ]
        self.assertEqual(MusicCSVStorage.open_library(Track, mock_csv), expected)

    def test_save_library(self):
        mock_csv = f"{self.DIRECTORY_PATH}test_writing_tracks.csv"
        mock_library = [Track("Trouble's Coming", "Royal Blood", "troubles_coming.mp3",
                              "6voIJ7OWwRabSZDC77D5Hp")]
        MusicCSVStorage.save_library(mock_library, mock_csv)
        file = open(mock_csv)
        self.assertEqual(
            str(file.read()), "Trouble's Coming,Royal Blood,troubles_coming.mp3,6voIJ7OWwRabSZDC77D5Hp\n"
        )
