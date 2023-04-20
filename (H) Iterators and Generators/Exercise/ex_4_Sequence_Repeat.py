# Create a class called sequence_repeat which should receive a sequence and a number upon initialization.
# Implement an iterator to return the given elements, so they form a string with a length - the given number.
# If the number is greater than the number of elements, then the sequence repeats as necessary.
class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.row = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.row += 1
        if self.index < len(self.sequence) and self.row <= self.number:
            self.index += 1
            return self.sequence[self.index-1]
        elif self.row <= self.number:
            self.index = 1
            return self.sequence[self.index-1]
        else:
            raise StopIteration()


# Test Code
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
