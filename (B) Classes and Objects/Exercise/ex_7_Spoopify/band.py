from typing import List
from Exercise.ex_7_Spoopify.album import Album


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        try:
            match = next(filter(lambda a: a.name == album_name, self.albums))
            if match.published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(match)
            return f"Album {album_name} has been removed."
        except StopIteration:
            return f"Album {album_name} is not found."

    def details(self) -> str:
        final = f"Band {self.name}\n"
        for album in self.albums:
            final += f"{album.details()}\n"
        return final
