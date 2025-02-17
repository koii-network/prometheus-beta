import os
import pytest
import tempfile
import shutil

from src.directory_checker import check_directory_exists

def test_existing_directory():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        assert check_directory_exists(temp_dir) == True

def test_non_existing_directory():
    # Use a path that is very unlikely to exist
    non_existent_dir = "/tmp/this_directory_should_not_exist_123456789"
    assert check_directory_exists(non_existent_dir) == False

def test_file_path():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        assert check_directory_exists(temp_file.name) == False

def test_empty_path():
    assert check_directory_exists("") == False

def test_none_input():
    with pytest.raises(TypeError):
        check_directory_exists(None)