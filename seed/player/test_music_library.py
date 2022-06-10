import unittest
from unittest.mock import Mock

from player.music_library import MusicLibrary, Track


class TestMusicLibrary(unittest.TestCase):
    DEFAULT_TRACKS = [
        Track("Never Come Back", "Caribou", "ncb.mp3",
              "https://open.spotify.com/track/0QEG3NGmWatNOIAVxudQfd"),
        Track("Light It Up - Remix", "Major Lazer", "light_it_up.mp3",
              "https://open.spotify.com/track/6GKkIuMAiGVDPUkwVESbqC"),
        Track("Trouble's Coming", "Royal Blood", "troubles_coming.mp3",
              "https://open.spotify.com/track/6voIJ7OWwRabSZDC77D5Hp"),
    ]

    def adds_tracks(self, library, tracks):
        """Helper method to add tracks to a music library instance under test
        :param library: MusicLibrary - instance of a library
        :param tracks: Array - tracks to be added as strings
        :returns: None
        """
        for track in tracks:
            library.add(track)

    def setUp(self):
        self.mock_storage = Mock()
        attrs = {'open_library.return_value': []}
        self.mock_storage.configure_mock(**attrs)

    def test_constructs(self):
        MusicLibrary(self.mock_storage)

    def test_add_does_not_throw_an_error(self):
        music_library = MusicLibrary(self.mock_storage)
        self.assertEqual(music_library.add("Rolling Blackouts by The Go! Team"), None)

    def test_all_returns_array_of_tracks(self):
        music_library = MusicLibrary(self.mock_storage)
        expected = ["Rolling Blackouts by The Go! Team"]
        self.adds_tracks(music_library, expected)
        self.assertEqual(music_library.all(), expected)

    def test_all_returns_multiple_tracks(self):
        music_library = MusicLibrary(self.mock_storage)
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        self.assertEqual(music_library.all(), self.DEFAULT_TRACKS)

    def test_removes_a_single_track_by_index(self):
        music_library = MusicLibrary(self.mock_storage)
        expected = [
            self.DEFAULT_TRACKS[0],
            self.DEFAULT_TRACKS[2],
        ]
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        music_library.remove(1)
        self.assertEqual(music_library.all(), expected)

    def test_remove_returns_true_on_success(self):
        music_library = MusicLibrary(self.mock_storage)
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        self.assertEqual(music_library.remove(1), True)

    def test_remove_returns_false_on_failure(self):
        music_library = MusicLibrary(self.mock_storage)
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        self.assertEqual(music_library.remove(20), False)

    def test_summarise_library(self):
        music_library = MusicLibrary(self.mock_storage)
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        expected = {
            "Caribou": 1,
            "Major Lazer": 1,
            "Royal Blood": 1,
        }
        self.assertEqual(music_library.summarise_library(), expected)

    def test_summarises__slightly_larger_library(self):
        music_library = MusicLibrary(self.mock_storage)
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        expected = {
            "Caribou": 2,
            "Major Lazer": 2,
            "Royal Blood": 2,
        }
        self.assertEqual(music_library.summarise_library(), expected)

    def test_searches_by_title(self):
        music_library = MusicLibrary(self.mock_storage)
        def mock_lambda(track): return "light" in track.title.lower()
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        music_library.search(mock_lambda)
        self.assertEqual(music_library.search(mock_lambda), [self.DEFAULT_TRACKS[1]])

    def test_searches_by_artist(self):
        music_library = MusicLibrary(self.mock_storage)
        def mock_lambda(track): return "caribou" in track.artist.lower()
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        music_library.search(mock_lambda)
        self.assertEqual(music_library.search(mock_lambda), [self.DEFAULT_TRACKS[0]])

    def test_searches_by_file(self):
        music_library = MusicLibrary(self.mock_storage)
        def mock_lambda(track): return "troubles_coming" in track.file.lower()
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        music_library.search(mock_lambda)
        self.assertEqual(music_library.search(mock_lambda), [self.DEFAULT_TRACKS[2]])

    def test_search_can_return_multiple_results(self):
        music_library = MusicLibrary(self.mock_storage)
        def mock_lambda(track): return "mp3" in track.file.lower()
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        music_library.search(mock_lambda)
        self.assertEqual(music_library.search(mock_lambda), self.DEFAULT_TRACKS)


class TestTrack(unittest.TestCase):
    def test_constructs(self):
        Track("Never Gonna Give You Up", "Rick Astley",
              "rick_roll.mp3", "4uLU6hMCjMI75M1A2tKUQC")

    def test_title_returns_correct_string(self):
        track = Track("Never Gonna Give You Up", "Rick Astley",
                      "rick_roll.mp3", "4uLU6hMCjMI75M1A2tKUQC")
        self.assertEqual(track.title, "Never Gonna Give You Up")

    def test_artist_returns_correct_string(self):
        track = Track("Never Gonna Give You Up", "Rick Astley",
                      "rick_roll.mp3", "4uLU6hMCjMI75M1A2tKUQC")
        self.assertEqual(track.artist, "Rick Astley")

    def test_file_returns_correct_string(self):
        track = Track("Never Gonna Give You Up", "Rick Astley",
                      "rick_roll.mp3", "4uLU6hMCjMI75M1A2tKUQC")
        self.assertEqual(track.file, "rick_roll.mp3")

    def test_link_returns_correct_string(self):
        track = Track("Never Gonna Give You Up", "Rick Astley",
                      "rick_roll.mp3", "4uLU6hMCjMI75M1A2tKUQC")
        self.assertEqual(
            track.link(), "https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC")

    def test_user_friendly_string_representation(self):
        track = Track("Never Gonna Give You Up", "Rick Astley",
                      "rick_roll.mp3", "4uLU6hMCjMI75M1A2tKUQC")
        self.assertEqual(str(track), "Never Gonna Give You Up by Rick Astley")
