import subprocess


class MusicPlayer:
    def __init__(self, subprocess=subprocess):
        self.subprocess = subprocess
        self.play_command = "afplay"
        self.stream_command = "open"

    def play(self, path):
        self.subprocess.call([self.play_command, path])

    def stream(self, link):
        self.subprocess.call([self.stream_command, link])
