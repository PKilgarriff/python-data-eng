import subprocess


class MusicPlayer:
    def __init__(self, subprocess=subprocess):
        self.subprocess = subprocess
        self.command = "afplay"

    def play(self, path):
        self.subprocess.call([self.command, path])
