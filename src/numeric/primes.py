from math import sqrt


def is_prime_number_compute(number: int) -> bool:
    """ Check if number is not divisible by [2...sqrt(number)] """
    limit = int(sqrt(number)) + 1
    return all(number % div != 0 for div in range(2, limit))


def is_prime_number_lookup(number: int) -> bool:
    """ Find in lookup table or compute if not found """
    # favorite, most used prime numbers
    primes = set([
        23,
        31,
        47,
        41,
    ])
    return True if number in primes else is_prime_number_compute(number)
