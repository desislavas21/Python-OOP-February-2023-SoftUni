# Create a generator function called read_next() which should receive a different number
# of arguments (all iterable). On each iteration, the function should return each element from each sequence.
def read_next(*args):
    for i_1 in args:
        for i_2 in i_1:
            yield i_2


# Test Code
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
print()
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
