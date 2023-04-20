# Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int).
# Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0)
# with the given step.
class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.operations_count = 0
        self.current = -step        # in order to balance the start

    def __iter__(self):
        return self

    def __next__(self):
        self.operations_count += 1
        if (self.operations_count - 1) < self.count:
            self.current = self.current + self.step
            return self.current
        else:
            raise StopIteration()

# Example
numbers = take_skip(2, 6)
for number in numbers:
    print(number)

# Example
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
