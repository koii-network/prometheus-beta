import os
import pytest
from datetime import datetime, timedelta
import time

from src.file_utils import get_file_last_modified_date

def test_get_file_last_modified_date_existing_file(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Get the last modified date
    modified_date = get_file_last_modified_date(str(test_file))
    
    # Check that the modified date is very recent (within last 5 seconds)
    assert isinstance(modified_date, datetime)
    assert datetime.now() - modified_date < timedelta(seconds=5)

def test_get_file_last_modified_date_nonexistent_file():
    # Test that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        get_file_last_modified_date("non_existent_file.txt")

def test_get_file_last_modified_date_invalid_input():
    # Test that TypeError is raised for non-string input
    with pytest.raises(TypeError):
        get_file_last_modified_date(123)

def test_get_file_last_modified_date_directory(tmp_path):
    # Test that OSError is raised for directory path
    with pytest.raises(OSError):
        get_file_last_modified_date(str(tmp_path))

def test_get_file_last_modified_date_changes(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Initial content")
    
    # Get initial modified date
    initial_modified_date = get_file_last_modified_date(str(test_file))
    
    # Wait a bit and modify the file
    time.sleep(1)
    test_file.write_text("Updated content")
    
    # Get new modified date
    new_modified_date = get_file_last_modified_date(str(test_file))
    
    # Check that the dates are different
    assert new_modified_date > initial_modified_date