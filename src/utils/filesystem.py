import os


def is_package_directory(path: str = None) -> bool:
    """
    Returns true if directory contains __init__.py file.
    """
    return True if '__init__.py' in os.listdir(path) else False
