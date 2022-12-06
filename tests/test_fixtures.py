import pytest


@pytest.fixture
def fixture_1():
    print("starting fixture 1")
    yield
    print("cleaning fixture 1")


@pytest.fixture(scope="function")
# @pytest.fixture(scope="module")
def fixture_2():
    print("starting fixture 2")
    yield
    print("cleaning fixture 2")


@pytest.fixture
def fixture_3():
    print("starting fixture 3")
    yield
    print("cleaning fixture 3")


@pytest.fixture
def fixture_4(fixture_3):
    print("starting fixture 4")
    yield
    print("cleaning fixture 4")


def test_1(fixture_1, fixture_2):
    pass


def test_2(fixture_4, fixture_2):
    pass
