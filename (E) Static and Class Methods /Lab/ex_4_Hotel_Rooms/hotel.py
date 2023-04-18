from Lab.ex_4_Hotel_Rooms.room import Room
from typing import List


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        try:
            match = [room for room in self.rooms if room.number == room_number][0]
            match.take_room(people)
        except IndexError:
            pass

    def free_room(self, room_number: int):
        try:
            match = [room for room in self.rooms if room.number == room_number][0]
            match.free_room()
        except IndexError:
            pass

    def status(self):
        return f"Hotel {self.name} has {sum(room.guests for room in self.rooms)} total guests\n" \
               f"Free rooms: {', '.join(str(room.number) for room in self.rooms if not room.is_taken)}\n" \
               f"Taken rooms: {', '.join(str(room.number) for room in self.rooms if room.is_taken)}"

