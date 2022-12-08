from dataclasses import dataclass

import pytest

from numeric.primes import is_prime_number_compute, is_prime_number_lookup


@pytest.fixture(params=[is_prime_number_compute, is_prime_number_lookup],
                ids=['compute', 'lookup'])
def algorithm(request):
    return request.param


@pytest.mark.parametrize("expect, number", ((True, 2), (False, 4), (True, 5), (True, 41)))
def test_is_prime_algorithm(algorithm, expect, number):
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


@dataclass
class Car:
    name: str
    year: int
    mileage: int

    def test_engine(self):
        print(f'checking engine in {self.name}')
        return True if self.year < 2010 or self.mileage < 100000 else False

    def test_brakes(self) -> bool:
        print(f'checking brakes in {self.name}')
        return True if self.year < 2018 else False


@pytest.fixture(params=[Car(name='Audi', year=2011, mileage=300000),
                        Car(name='Honda', year=2015, mileage=90000)], ids=lambda x: x.name)
def car(request):
    return request.param


@pytest.mark.parametrize('test_type',
                         ((lambda x: x.test_brakes()), (lambda x: x.test_engine())),
                         ids=['check brakes', 'check engine'])
def test_car(car, test_type):
    assert test_type(car)
