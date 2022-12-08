import abc
from unittest.mock import Mock, ANY, MagicMock

import pytest


def test_how_mock_works():
    mock = Mock()
    assert 'create_user' not in mock.__dir__()
    mock.create_user('Bob')
    assert 'create_user' in mock.__dir__()
    assert isinstance(mock.create_user, Mock)
    mock.create_user.assert_called_once_with('Bob')


# --- asserts


def test_mock_with_asserts():
    """
    How does a mock work?

    Calling mock.add_user('Bob') creates a new mock (add_user).
    """
    mock = Mock()
    mock.add_user('Bob')

    mock.add_user.assert_called_once()
    mock.add_user.assert_called_once_with('Bob')
    mock.add_user.assert_called_once_with(ANY)
    # mock.add_user.assert_called_once_with('Joe')

    mock.delete_user.assert_not_called()


# --- side effects

def test_mock_with_side_effect():
    """
    mock with side effect
    """

    # callable
    mock = Mock()
    mock.side_effect = lambda: print("calling this mock has side effects")
    # calling mock should execute callable assigned as 'side_effect'
    mock()

    # iterable
    mock = Mock()
    mock.side_effect = (1, 2)
    print(mock())
    print(mock())
    # print(mock()) # -> StopIteration

    # exception
    mock = Mock()
    mock.side_effect = ValueError("wrong value")
    with pytest.raises(ValueError):
        mock()


# --- Mock vs MagicMock


def test_with_mock():
    """
    Regular Mock does not allow to replace magic methods
    """
    mock = Mock()
    assert not isinstance(mock.__str__, MagicMock)
    mock.__str__.return_value = "no magic"
    print(mock)


def test_with_magic_mock():
    """
    MagicMock replaces magic methods (__xyz__)
    """
    mock = MagicMock()
    assert isinstance(mock.__str__, MagicMock)
    mock.__str__.return_value = "magic!"
    print(mock)


def test_with_strict_mock():
    """
    Mock cna be restricted to only specific methods
    """
    mock = Mock(spec=['create', 'delete'])
    mock.create = Mock()


class RadioController(abc.ABC):
    """
    Interface for controlling a radio.
    """

    @abc.abstractmethod
    def turn_on(self) -> None:
        ...

    def turn_off(self) -> None:
        ...

    def set_station(self, number: int) -> None:
        ...


def test_with_strict_mock_after_class():
    """
    Mock can be restricted to only specific methods.
    """
    mock = Mock(spec=RadioController)
    mock.create = Mock()
    mock.turn_on()
    # mock.volume_up() # -> AttributeError
    mock.turn_off()
