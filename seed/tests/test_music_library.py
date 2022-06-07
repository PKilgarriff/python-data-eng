import unittest

from player.music_library import MusicLibrary


class TestMusicLibrary(unittest.TestCase):
    def adds_tracks(self, library, tracks):
        """Helper method to add tracks to a music library instance under test
        :param library: MusicLibrary - instance of a library
        :param tracks: Array - tracks to be added as strings
        :returns: None
        """
        for track in tracks:
            library.add(track)

    def test_constructs(self):
        MusicLibrary()

    def test_add_does_not_throw_an_error(self):
        music_library = MusicLibrary()
        self.assertEqual(music_library.add("Rolling Blackouts by The Go! Team"), None)

    def test_all_returns_array_of_tracks(self):
        music_library = MusicLibrary()
        expected = ["Rolling Blackouts by The Go! Team"]
        self.adds_tracks(music_library, expected)
        self.assertEqual(music_library.all(), expected)

    def test_all_returns_multiple_tracks(self):
        music_library = MusicLibrary()
        expected = ["Rolling Blackouts by The Go! Team",
                    "Oh Yeah by Locust", "Sleep on the Wing by Bibio"]
        self.adds_tracks(music_library, expected)
        self.assertEqual(music_library.all(), expected)

    def test_removes_a_single_track_by_index(self):
        music_library = MusicLibrary()
        input = ["Rolling Blackouts by The Go! Team",
                 "Oh Yeah by Locust", "Sleep on the Wing by Bibio"]
        expected = ["Rolling Blackouts by The Go! Team", "Sleep on the Wing by Bibio"]
        self.adds_tracks(music_library, input)
        music_library.remove(1)
        self.assertEqual(music_library.all(), expected)

    def test_remove_returns_true_on_success(self):
        music_library = MusicLibrary()
        input = ["Rolling Blackouts by The Go! Team",
                 "Oh Yeah by Locust", "Sleep on the Wing by Bibio"]
        self.adds_tracks(music_library, input)
        self.assertEqual(music_library.remove(1), True)

    def test_remove_returns_false_on_failure(self):
        music_library = MusicLibrary()
        input = ["Rolling Blackouts by The Go! Team"]
        self.adds_tracks(music_library, input)
        self.assertEqual(music_library.remove(20), False)
