# Create a class called countdown_iterator. Upon initialization, it should receive a count. Implement the iterator
# to return each countdown number (from count to 0 inclusive), separated by a single space.
class countdown_iterator:

    def __init__(self, count: int):
        self.count = count
        self.step = 0

    def __iter__(self):
        return self

    def __next__(self):
        step = self.step
        self.step += 1
        if step <= self.count:
            return self.count - step
        else:
            raise StopIteration()


# Test Code
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
print()
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
