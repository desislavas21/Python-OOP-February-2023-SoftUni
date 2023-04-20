# Create a generator function called get_primes() which should receive a list of integer numbers and return
# a list containing only the prime numbers from the initial list.
def get_primes(numbers):
    for n in [x for x in numbers if x >= 2]:  #prime numbers are positive numbers and greater than one
        prime = True
        for i in range(1, n):
            if i != 1 and n % i == 0:
                prime = False
        if prime:
            yield n


# Test Code
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
