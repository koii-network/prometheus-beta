import os
import pytest
import tempfile
import shutil

from src.directory_utils import directory_exists

def test_directory_exists_valid_directory():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        assert directory_exists(temp_dir) == True

def test_directory_exists_non_existent_directory():
    # Generate a path that doesn't exist
    non_existent_path = "/path/to/non/existent/directory"
    assert directory_exists(non_existent_path) == False

def test_directory_exists_file_instead_of_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert directory_exists(temp_file_path) == False
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_directory_exists_relative_path():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Get the relative path
        current_dir = os.getcwd()
        relative_path = os.path.relpath(temp_dir, current_dir)
        
        assert directory_exists(relative_path) == True