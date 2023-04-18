from Exercise.ex_7_Spoopify.song import Song
from typing import List


class Album:

    def __init__(self, name: str, *songs):
        self.name = name
        self.songs: List[Song] = list(songs)
        self.published = False

    def add_song(self, song: Song) -> str:
        if not self.published:
            if song.single:
                return f"Cannot add {song.name}. It's a single"
            if song in self.songs:
                return "Song is already in the album."
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

        else:
            return "Cannot add songs. Album is published."

    def remove_song(self, song_name: str) -> str:
        if not self.published:
            try:
                match = next(filter(lambda s: s.name == song_name, self.songs))
                self.songs.remove(match)
                return f"Removed song {song_name} from album {self.name}."
            except StopIteration:
                return "Song is not in the album."
        else:
            return "Cannot remove songs. Album is published."

    def publish(self) -> str:
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self) -> str:
        final = f"Album {self.name}\n"
        for song in self.songs:
            final += f"== {song.get_info()}\n"
        return final
