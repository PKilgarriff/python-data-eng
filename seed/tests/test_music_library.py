import unittest

from player.music_library import MusicLibrary, Track


class TestMusicLibrary(unittest.TestCase):
    DEFAULT_TRACKS = ["Rolling Blackouts by The Go! Team",
                      "Oh Yeah by Locust", "Sleep on the Wing by Bibio"]

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
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        self.assertEqual(music_library.all(), self.DEFAULT_TRACKS)

    def test_removes_a_single_track_by_index(self):
        music_library = MusicLibrary()
        expected = ["Rolling Blackouts by The Go! Team", "Sleep on the Wing by Bibio"]
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        music_library.remove(1)
        self.assertEqual(music_library.all(), expected)

    def test_remove_returns_true_on_success(self):
        music_library = MusicLibrary()
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        self.assertEqual(music_library.remove(1), True)

    def test_remove_returns_false_on_failure(self):
        music_library = MusicLibrary()
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        self.assertEqual(music_library.remove(20), False)


class TestTrack(unittest.TestCase):
    def test_constructs(self):
        Track("The Boys of Summer", "DJ Sammy", "summer.mp3")

    def test_title_returns_correct_string(self):
        track = Track("The Boys of Summer", "DJ Sammy", "summer.mp3")
        self.assertEqual(track.title, "The Boys of Summer")

    def test_artist_returns_correct_string(self):
        track = Track("The Boys of Summer", "DJ Sammy", "summer.mp3")
        self.assertEqual(track.artist, "DJ Sammy")

    def test_file_returns_correct_string(self):
        track = Track("The Boys of Summer", "DJ Sammy", "summer.mp3")
        self.assertEqual(track.file, "summer.mp3")

    def test_user_friendly_string_representation(self):
        track = Track("The Boys of Summer", "DJ Sammy", "summer.mp3")
        self.assertEqual(str(track), "The Boys of Summer by DJ Sammy")
