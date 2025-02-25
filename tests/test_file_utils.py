import os
import pytest
from datetime import datetime
import time

from src.file_utils import get_file_last_modified_date

def test_get_file_last_modified_date():
    # Create a temporary file
    test_file_path = 'tests/test_file.txt'
    
    # Create the file and write some content
    with open(test_file_path, 'w') as f:
        f.write('Test content')
    
    try:
        # Get the last modified date
        last_modified = get_file_last_modified_date(test_file_path)
        
        # Check if it's a datetime object
        assert isinstance(last_modified, datetime)
        
        # Check if the last modified time is very recent (within 1 second)
        assert (datetime.now() - last_modified).total_seconds() < 1
    
    finally:
        # Clean up the test file
        os.remove(test_file_path)

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        get_file_last_modified_date('non_existent_file.txt')

def test_invalid_input():
    with pytest.raises(TypeError):
        get_file_last_modified_date(123)  # Non-string input

def test_timestamp_accuracy():
    # Create a file and modify it
    test_file_path = 'tests/timestamp_test.txt'
    
    # Create initial file
    with open(test_file_path, 'w') as f:
        f.write('Initial content')
    
    # Wait a bit to ensure timestamp changes
    time.sleep(1)
    
    # Modify the file
    with open(test_file_path, 'w') as f:
        f.write('Updated content')
    
    try:
        # Get last modified date
        last_modified = get_file_last_modified_date(test_file_path)
        
        # Check if last modified is recent
        time_diff = (datetime.now() - last_modified).total_seconds()
        assert time_diff < 2, f"Time difference too large: {time_diff} seconds"
    
    finally:
        # Clean up the test file
        os.remove(test_file_path)