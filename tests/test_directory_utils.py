import os
import tempfile
import shutil
import pytest
from src.directory_utils import check_directory_exists

def test_directory_exists():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Check that the existing directory returns True
        assert check_directory_exists(temp_dir) == True

def test_directory_does_not_exist():
    # Create a path that definitely does not exist
    non_existent_dir = "/path/to/definitely/nonexistent/directory"
    assert check_directory_exists(non_existent_dir) == False

def test_file_is_not_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        assert check_directory_exists(temp_file.name) == False

def test_none_input():
    with pytest.raises(TypeError):
        check_directory_exists(None)

def test_invalid_type_input():
    with pytest.raises(TypeError):
        check_directory_exists(123)  # Integer instead of string