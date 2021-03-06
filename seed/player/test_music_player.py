import unittest
from unittest.mock import Mock
from player.music_player import MusicPlayer


class TestMusicPlayer(unittest.TestCase):
    YODEL_PATH = "/Users/paul/Projects/Makers/bridge_week_01/phase_2/python-data-engineering-challenges/seed/data/tunes/myfav.wav"
    SPOTIFY_LINK = "https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC"

    def test_constructs(self):
        mock_subprocess = Mock()
        MusicPlayer(mock_subprocess)

    def test_play_calls_subprocess(self):
        mock_subprocess = Mock()
        music_player = MusicPlayer(mock_subprocess)
        music_player.play(self.YODEL_PATH)
        mock_subprocess.call.assert_called_with(["afplay", self.YODEL_PATH])

    def test_play_calls_subprocess(self):
        mock_subprocess = Mock()
        music_player = MusicPlayer(mock_subprocess)
        music_player.stream(self.SPOTIFY_LINK)
        mock_subprocess.call.assert_called_with(["open", self.SPOTIFY_LINK])
