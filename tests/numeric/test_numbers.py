from dataclasses import dataclass

import pytest

from numeric.numbers import is_square_number, fizz_buzz, average, is_arithmetic_sequence


# Simple test

def test_is_square_number():
    assert is_square_number(5) == False


test_data = (
    (True, 1),
    (False, 2),
)


# Parametrized test

@pytest.mark.parametrize("expect, number", test_data)
def test_is_square_number_parameterized(expect, number):
    assert expect == is_square_number(number)


# Parametrized test with custom description

@pytest.mark.parametrize("expect, number", test_data, ids=("One - yes", "Two - no"))
def test_is_square_number_parameterized_custom_ids(expect, number):
    assert expect == is_square_number(number)


# Parametrized test with custom description generated through function

def param_to_string(arg):
    if isinstance(arg, bool):
        return f'Expected: {arg}'
    elif isinstance(arg, int):
        return f'Number: {arg}'


@pytest.mark.parametrize("expect, number", test_data, ids=param_to_string)
def test_is_square_number_parameterized_ids_function(expect, number):
    assert expect == is_square_number(number)


# Parametrized test with single aggregating parameter

@dataclass(frozen=True)
class Param:
    expect: bool
    number: int


@pytest.mark.parametrize("param", (Param(False, 3), Param(True, 4)), ids=lambda p: str(p))
def test_is_square_number_parameterized_dataclass(param):
    assert param.expect == is_square_number(param.number)


@pytest.mark.parametrize("expect, number",
                         (('1', 1), ('Fizz', 3), ('Buzz', 5), ('FizzBuzz', 15), ('-4', -4)))
def test_fizz_buzz(expect, number):
    assert expect == fizz_buzz(number)

