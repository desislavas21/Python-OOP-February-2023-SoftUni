# Create a class called reverse_iter which should receive an iterable upon initialization.
# Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.
class reverse_iter:

    def __init__(self, some_i):
        self.some_iterable = some_i[::-1]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.some_iterable):
            self.index += 1
            return self.some_iterable[self.index - 1]
        else:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
