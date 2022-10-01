"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2
    count = 0

    if number_of_primes <= 0:
        raise ValueError

    while count < number_of_primes:

        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                break
        else:
            list.append(num);
            count += 1
        num += 1

    return list