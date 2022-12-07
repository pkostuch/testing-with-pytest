import pytest

from numeric.primes import is_prime_number_sieve, is_prime_number_lookup


@pytest.fixture(params=[is_prime_number_sieve, is_prime_number_lookup],
                ids=['sieve', 'lookup'])
def algorithm(request):
    return request.param


@pytest.mark.parametrize("expect, number", ((True, 2), (False, 4), (True, 5), (True, 41)))
def test_is_package_directory_with_parametrized_fixture(algorithm, expect, number):
    assert expect == algorithm(number)
