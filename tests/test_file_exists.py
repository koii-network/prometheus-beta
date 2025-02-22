import os
import pytest
from src.file_exists import is_file_exists

def test_existing_file():
    # Test with an existing file in the repository
    assert is_file_exists('README.md') == True
    assert is_file_exists('requirements.txt') == True

def test_non_existing_file():
    # Test with a non-existing file
    assert is_file_exists('non_existent_file.txt') == False

def test_file_path_types():
    # Test with different path types
    assert is_file_exists('./README.md') == True
    assert is_file_exists('.gitignore') == True

def test_absolute_path():
    # Test with absolute path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    abs_readme_path = os.path.join(parent_dir, 'README.md')
    assert is_file_exists(abs_readme_path) == True