# Create a generator function called possible_permutations() which should receive a list and return lists
# with all possible permutations between its elements.
from itertools import permutations


def possible_permutations(numbers: list):
    for number in list(permutations(numbers)):
        yield list(number)


# Test Code
[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
