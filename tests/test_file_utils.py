import os
import pytest
from src.file_utils import file_exists

def test_file_exists_with_existing_file():
    # Test with an existing file in the repository
    assert file_exists('.gitignore') == True
    assert file_exists('README.md') == True
    assert file_exists('requirements.txt') == True

def test_file_exists_with_non_existing_file():
    # Test with a non-existing file
    assert file_exists('non_existent_file.txt') == False

def test_file_exists_with_directory():
    # Ensure function returns False for directories
    assert file_exists('.') == False
    assert file_exists('src') == False

def test_file_exists_with_invalid_path():
    # Test with invalid path types
    with pytest.raises(TypeError):
        file_exists(None)
    with pytest.raises(TypeError):
        file_exists(123)