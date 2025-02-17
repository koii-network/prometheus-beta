import os
import pytest
from src.file_utils import file_exists

def test_file_exists_valid_file():
    # Test with an existing file in the repository
    assert file_exists('.gitignore') == True
    assert file_exists('README.md') == True
    assert file_exists('requirements.txt') == True

def test_file_exists_nonexistent_file():
    # Test with a non-existent file
    assert file_exists('nonexistent_file.txt') == False

def test_file_exists_empty_path():
    # Test with an empty path
    assert file_exists('') == False

def test_file_exists_none_input():
    # Test with None input
    with pytest.raises(TypeError):
        file_exists(None)