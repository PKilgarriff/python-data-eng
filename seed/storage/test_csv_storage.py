import unittest

from player.music_library import Track
from storage.csv_storage import MusicCSVStorage


class TestMusicPlayer(unittest.TestCase):
    def test_constructs(self):
        MusicCSVStorage()

    def test_open(self):
        mock_csv = "/Users/paul/Projects/Makers/bridge_week_01/phase_2/python-data-engineering-challenges/seed/storage/test_tracks.csv"
        storage = MusicCSVStorage()
        storage.open(mock_csv)
        expected = [
            Track("Never Come Back", "Caribou", "ncb.mp3",
                  "0QEG3NGmWatNOIAVxudQfd"),
            Track("Light It Up - Remix", "Major Lazer", "light_it_up.mp3",
                  "6GKkIuMAiGVDPUkwVESbqC"),
            Track("Trouble's Coming", "Royal Blood", "troubles_coming.mp3",
                  "6voIJ7OWwRabSZDC77D5Hp"),
        ]
        self.assertEqual(storage.tracks, expected)


# file_path agnostic
# file_type csv
# import the CSV stuff
# return an array of items
