from math import sqrt


def is_prime_number_sieve(number: int) -> bool:
    limit = int(sqrt(number)) + 1
    return all(number % div != 0 for div in range(2, limit))


def is_prime_number_lookup(number: int) -> bool:
    primes = {
        2: True,
        3: True,
        4: False,
        5: True,
        6: False,
        7: True,
        8: False,
        9: False,
        10: False,
        11: True
    }
    return primes.get(number, is_prime_number_sieve(number))
