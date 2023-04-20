# Create a class called vowels, which should receive a string. Implement the __iter__ and __next__
# methods, so the iterator returns only the vowels from the string.
class vowels:

    def __init__(self, some_str: str):
        self.vowels = ["a", "e", "i", "u", "y", "o"]
        self.some_str = [x for x in some_str if x.lower() in self.vowels]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.some_str):
            self.index += 1
            if (self.index - 1) < len(self.some_str):
                return self.some_str[self.index - 1]
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)