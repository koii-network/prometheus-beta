import os
import pytest
from src.file_exists import check_file_exists

def test_check_file_exists_existing_file():
    # Use an existing file in the repository for testing
    existing_file = 'README.md'
    assert check_file_exists(existing_file) is True

def test_check_file_exists_non_existing_file():
    # Test a non-existing file
    non_existing_file = 'non_existent_file.txt'
    assert check_file_exists(non_existing_file) is False

def test_check_file_exists_empty_path():
    # Test with an empty path
    with pytest.raises(TypeError):
        check_file_exists()

def test_check_file_exists_none_path():
    # Test with None as path
    assert check_file_exists(None) is False

def test_check_file_exists_directory():
    # Test with a directory path
    assert check_file_exists('.') is False