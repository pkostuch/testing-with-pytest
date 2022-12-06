from unittest.mock import patch, MagicMock

import numeric
from utils.filesystem import is_package_directory

"""
Demonstrates how mock.patch can be used.
"""


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
