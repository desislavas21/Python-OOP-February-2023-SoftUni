# Implement the three generator functions:
# •	integers() - generates an infinite amount of integers (starting from 1)
# •	halves() - generates the halves of those integers (each integer / 2)
# •	take(n, seq) - takes the first n halves of those integers
def solution():

    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():

        for i in integers():
            yield i/2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return (take, halves, integers)


# Test Code
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
