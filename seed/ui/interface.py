# Over to you!
# I'm outta here!
# ~Kez xoxo

from player.music_library import MusicLibrary, Track
from player.music_player import MusicPlayer


class Interface:
    def __init__(self, console, storage, subprocess):
        self.console = console
        self.music_library = MusicLibrary(storage)
        self.music_player = MusicPlayer(subprocess)

# TODO convert this into a dictionary?
    def run(self):
        self.console.print("Welcome to your music library!")
        while True:
            choice = self._prompt()
            if choice == "a":
                self._add_track()
            elif choice == "p":
                self._play_track()
            elif choice == "o":
                self._stream_track()
            elif choice == "d":
                self._remove_track()
            elif choice == "l":
                self._list_tracks(self.music_library.all())
            elif choice == "s":
                self._search_tracks()
            elif choice == "S":
                self._summarise_tracks()
            elif choice == "q":
                return
            else:
                self.console.print("No such command! Try again.")

    def _prompt(self):
        self.console.print("Enter:")
        self.console.print("  a: to add a track")
        self.console.print("  p: to play a track")
        self.console.print("  o: to open Spotify for a track")
        self.console.print("  d: to delete a track")
        self.console.print("  l: to list your tracks")
        self.console.print("  s: to search your tracks")
        self.console.print("  S: to summarise your top 15 artists")
        self.console.print("  q: to quit")
        return self.console.input("What do you pick? ")

    def _add_track(self):
        title = self.console.input("What's the title? ")
        artist = self.console.input("What's the artist? ")
        file = self.console.input("What's the file? ")
        self.music_library.add(Track(title, artist, file))
        self.console.print("Added successfully.")

    def _list_tracks(self, tracks):
        for idx, track in enumerate(tracks):
            self.console.print(
                f"{idx + 1}. {track.title} by {track.artist} @ {track.file}"
            )

# TODO Further refactor the Searchers so this doesn't need a conditional
# TODO Allow user to play or stream from search results
    def _search_tracks(self):
        self.console.print("Search by:")
        self.console.print("  t: title")
        self.console.print("  a: artist")
        self.console.print("  f: file")
        self.console.print("  *: anything")
        choice = self.console.input("What do you want to search by? ")
        search = self.console.input("What do you want to search for? ").lower()
        if choice == "t":
            found = self.music_library.search(
                Searchers.by_title_case_insensitive(search)
            )
            self._list_tracks(found)
        elif choice == "a":
            found = self.music_library.search(
                Searchers.by_artist_case_insensitive(search)
            )
            self._list_tracks(found)
        elif choice == "f":
            found = self.music_library.search(
                Searchers.by_file_case_insensitive(search)
            )
            self._list_tracks(found)
        elif choice == "*":
            found = self.music_library.search(
                Searchers.by_any_field_case_insensitive(search)
            )
            self._list_tracks(found)
        else:
            self.console.print("No such field!")

    def _summarise_tracks(self):
        summary = self.music_library.summarise_library()
        for index, (artist, track_count) in enumerate(summary.items()):
            self.console.print(f"{index + 1}. {artist}: {track_count} tracks")

# TODO Extract the shared logic from the _play_track and _stream_track methods
    def _play_track(self):
        self._list_tracks(self.music_library.all())
        track_id = int(self.console.input("Which do you want to play? ")) - 1
        tracks = self.music_library.all()
        if track_id >= 0 and track_id < len(tracks):
            track = tracks[track_id]
            self.console.print(f"Playing {track.title} by {track.artist}...")
            self.music_player.play(track.file)
            self.console.print("Done.")
        else:
            self.console.print("No such track.")

    def _stream_track(self):
        self._list_tracks(self.music_library.all())
        track_id = int(self.console.input("Which do you want to stream? ")) - 1
        tracks = self.music_library.all()
        if track_id >= 0 and track_id < len(tracks):
            track = tracks[track_id]
            self.console.print(f"Streaming {track.title} by {track.artist}...")
            self.music_player.stream(track.link())
            self.console.print("Done.")
        else:
            self.console.print("No such track.")

    def _remove_track(self):
        self._list_tracks(self.music_library.all())
        track_id = int(self.console.input("Which do you want to delete? ")) - 1
        if self.music_library.remove(track_id):
            self.console.print("Deleted successfully.")
        else:
            self.console.print("No such track.")


class ConsoleIO:
    def print(self, message):
        print(message)

    def input(self, prompt=None):
        if prompt is None:
            return input()
        return input(prompt)


class Searchers:
    # def by_term_case_insensitive(search_term, search_field):
    #     return lambda track: search_term.lower() in track[search_field].lower()

    def by_title_case_insensitive(search_term):
        return lambda track: search_term.lower() in track.title.lower()

    def by_artist_case_insensitive(search_term):
        return lambda track: search_term.lower() in track.artist.lower()

    def by_file_case_insensitive(search_term):
        return lambda track: search_term.lower() in track.file.lower()

    def by_any_field_case_insensitive(search_term):
        return lambda track: (search_term.lower() in track.title.lower() or
                              search_term.lower() in track.artist.lower() or
                              search_term.lower() in track.file.lower())
