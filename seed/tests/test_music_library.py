import unittest

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
        expected = [
            "Never Come Back by Caribou",
            "Light It Up - Remix by Major Lazer",
            "Trouble's Coming by Royal Blood"
        ]
        self.adds_tracks(music_library, self.DEFAULT_TRACKS)
        self.assertEqual(music_library.all(), expected)

    def test_removes_a_single_track_by_index(self):
        music_library = MusicLibrary()
        expected = [
            "Never Come Back by Caribou",
            "Trouble's Coming by Royal Blood"
        ]
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
