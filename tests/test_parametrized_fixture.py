import pytest

from numeric.primes import is_prime_number_sieve, is_prime_number_lookup


@pytest.fixture(params=[is_prime_number_sieve, is_prime_number_lookup],
                ids=['sieve', 'lookup'])
def algorithm(request):
    return request.param


@pytest.mark.parametrize("expect, number", ((True, 2), (False, 4), (True, 5), (True, 41)))
def test_is_package_directory_with_parametrized_fixture(algorithm, expect, number):
    assert expect == algorithm(number)


@pytest.fixture(params=["Hello!", "Hi!"])
def hello(request):
    return request.param


@pytest.fixture(params=["Bye!", "Good bye!"])
def bye(request):
    return request.param


@pytest.mark.parametrize("question", ["How are you?", "How do you do?"])
def test_greetings(hello, question, bye):
    """ Multiple parametrized fixtures"""
    print(f'{hello}, {question}, {bye}')


@pytest.fixture(params=["Morning!", "Hey!"])
def hello_bye(request, bye):
    return f'{request.param}, {bye}'


@pytest.mark.parametrize("question", ["How are you?", "How do you do?"])
def test_greetings(hello, question, bye):
    """ Multiple parametrized fixtures"""
    print(f'{hello}, {question}, {bye}')


@pytest.mark.parametrize("question", ["How are you?", "How do you do?"])
def test_greetings_hierarchy(hello_bye, question):
    """ Multiple parametrized fixtures"""
    print(f'{hello_bye}, {question}')