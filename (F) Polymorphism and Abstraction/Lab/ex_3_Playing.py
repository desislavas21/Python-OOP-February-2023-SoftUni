# Create a function called start_playing which will return its play() method.

def start_playing(any_type):
    return any_type.play()


# Example
class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))


class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))
