def fibonacci():
    previous = -1
    current = 1
    while True:
        next = previous + current
        yield next
        previous = current
        current = next

# Test Code
generator = fibonacci()
for i in range(5):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))
