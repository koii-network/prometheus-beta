import os
import pytest
import tempfile
from src.directory_utils import directory_exists

def test_directory_exists_true():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        assert directory_exists(temp_dir) == True

def test_directory_exists_false():
    # Use a path that is extremely unlikely to exist
    non_existent_dir = "/tmp/surely_this_directory_does_not_exist_123456"
    assert directory_exists(non_existent_dir) == False

def test_directory_exists_with_file():
    # Create a temporary file 
    with tempfile.NamedTemporaryFile() as temp_file:
        assert directory_exists(temp_file.name) == False

def test_directory_exists_empty_string():
    assert directory_exists("") == False

def test_directory_exists_none():
    with pytest.raises(TypeError):
        directory_exists(None)