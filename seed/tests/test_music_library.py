import unittest

from player.music_library import MusicLibrary


class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        MusicLibrary()

    def test_add_does_not_throw_an_error(self):
        music_library = MusicLibrary()
        self.assertEqual(music_library.add("Rolling Blackouts by The Go! Team"), None)


"""
>> > music_library = MusicLibrary()
>> > music_library.add("Rolling Blackouts by The Go! Team")
None
>> > music_library.add("Oh Yeah by Locust")
None
>> > music_library.add("Sleep on the Wing by Bibio")
None
>> > music_library.all()
["Rolling Blackouts by The Go! Team", "Oh Yeah by Locust", "Sleep on the Wing by Bibio"]
>> > music_library.remove(1)  # Removes track 1
True  # Returns True on successful removal
>> > music_library.remove(20)  # If you remove a track that doesn't exist...
False  # It should return False
>> > music_library.all()
["Rolling Blackouts by The Go! Team", "Sleep on the Wing by Bibio"]
"""
