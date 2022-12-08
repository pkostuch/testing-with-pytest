"""
Demonstrates how mock.patch can be used.
"""
import os
from unittest.mock import patch, MagicMock

import numeric
from utils.filesystem import is_package_directory


def test_is_package_directory():
    """
    Patch os.listdir function.
    """
    with patch("os.listdir", MagicMock(return_value=['foo.py', '__init__.py'])) as mock:
        assert is_package_directory('/tmp')
        mock.assert_called_once_with('/tmp')


def test_add_with_patch():
    """
    Patch 'numeric.numbers.add using callable
    """
    with patch('numeric.numbers.add', lambda a, b: a * b):
        assert 20 == numeric.numbers.add(4, 5)


def test_patch_simple_example():
    """ Path as context manager """
    with patch('os.mkdir', MagicMock()) as mock:
        os.mkdir('/tmp')
        mock.assert_called_once_with('/tmp')


@patch('os.listdir')
def test_patch_decorator(mock):  # argument 'mock' is created by @patch
    """ patch as function decorator """
    mock.return_value = ['home', 'tmp']
    os.listdir()
    mock.assert_called_once()


@patch('os.listdir')
@patch('os.mkdir')
def test_patch_decorators(mock_mkdir, mock_listdir):  # more than @patch can be specified
    """ multiple decorators """
    os.mkdir('/tmp')
    os.listdir()
    mock_listdir.assert_called_once()
    mock_mkdir.assert_called_once_with('/tmp')
