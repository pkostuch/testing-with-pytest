import math
from typing import List


def is_square_number(number: int) -> bool:
    sq = int(math.sqrt(number))
    return sq * sq == number


def is_triangle_number(number: int) -> bool:
    """
    Checks is a given number is a triangle number (1, 3, 6, 10, ...)

    >>> is_triangle_number(3)
    True
    >>> is_triangle_number(5)
    False
    """
    return is_square_number(8 * number + 1)


def fizz_buzz(number) -> str:
    divisible_by_3 = number % 3 == 0
    divisible_by_5 = number % 5 == 0
    if divisible_by_3 and divisible_by_5:
        return "FizzBuzz"
    if divisible_by_3:
        return "Fizz"
    if divisible_by_5:
        return "Buzz"
    return str(number)


def is_arithmetic_sequence(numbers: List[int]) -> bool:
    """
    >>> is_arithmetic_sequence([1,2,3,4])
    True
    >>> is_arithmetic_sequence([1,2,4])
    False
    >>> is_arithmetic_sequence([4,7,10,13])
    True
    """
    if len(numbers) < 2:
        return True
    diff = numbers[1] - numbers[0]
    return all(b - a == diff for a, b in zip(numbers, numbers[1:]))


def add(a, b):
    """
    >>> add(1, 3)
    4
    """
    return a + b
