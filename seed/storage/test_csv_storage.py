import unittest

from player.music_player import Track
from storage.csv_storage import MusicCSVStorage


class TestMusicPlayer(unittest.TestCase):
    def test_constructs(self):
        MusicCSVStorage()

    def test_open(self):
        mock_csv = "title_1,artist_1,file_1,link_1"
        storage = MusicCSVStorage()
        storage.open(mock_csv)
        self.assertEqual(storage.tracks, [Track(
            "title_1", "artist_1", "file_1", "link_1")])


# file_path agnostic
# file_type csv
# import the CSV stuff
# return an array of items
