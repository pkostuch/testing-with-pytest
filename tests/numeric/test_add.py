"""
unit tests for functions - skip, xfail
"""
import pytest

from numeric.numbers import add


# "basic" test
def test_add_basic():
    assert add(1, 4) == 5


# parameterized test
@pytest.mark.parametrize("expect, a, b", ((4, 2, 2), (4, 1, 3)))
def test_add(expect, a, b):
    assert expect == add(a, b)


@pytest.mark.skip(reason="negative numbers are not supported")
def test_add_skipped():
    assert add(2, -1) == 1


@pytest.mark.xfail
def test_add_xfail():
    assert add(2, 0) == 1
