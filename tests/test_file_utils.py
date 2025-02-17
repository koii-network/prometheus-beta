import os
import pytest
from src.file_utils import file_exists

def test_file_exists_existing_file():
    # Test with .gitignore which we know exists
    assert file_exists('.gitignore') == True

def test_file_exists_non_existing_file():
    # Test with a file that definitely doesn't exist
    assert file_exists('nonexistent_file.txt') == False

def test_file_exists_directory():
    # Ensure function returns False for directories
    assert file_exists('.') == False

def test_file_exists_empty_path():
    # Test with empty path
    assert file_exists('') == False

def test_file_exists_absolute_path():
    # Test with absolute path
    current_dir = os.path.abspath('.')
    gitignore_path = os.path.join(current_dir, '.gitignore')
    assert file_exists(gitignore_path) == True