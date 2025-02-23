import os
import pytest
from datetime import datetime
import time

from src.file_modified_date import get_file_last_modified_date

def test_get_file_last_modified_date():
    # Create a temporary file
    test_file_path = 'tests/test_file.txt'
    
    # Create the file and write something to it
    with open(test_file_path, 'w') as f:
        f.write('Test content')
    
    try:
        # Get the last modified date
        modified_date = get_file_last_modified_date(test_file_path)
        
        # Check that it returns a datetime object
        assert isinstance(modified_date, datetime)
        
        # Check that the modified date is recent (within last 5 seconds)
        time_diff = datetime.now() - modified_date
        assert time_diff.total_seconds() < 5
    
    finally:
        # Clean up the test file
        os.remove(test_file_path)

def test_file_not_found():
    # Test that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        get_file_last_modified_date('non_existent_file.txt')

def test_invalid_input_type():
    # Test that TypeError is raised for non-string input
    with pytest.raises(TypeError):
        get_file_last_modified_date(123)

def test_file_path_validation():
    # Ensure function works with relative and absolute paths
    # Create a file to test
    test_file_path = 'tests/validation_test_file.txt'
    
    with open(test_file_path, 'w') as f:
        f.write('Validation test')
    
    try:
        # Test with relative path
        mod_date_relative = get_file_last_modified_date(test_file_path)
        assert isinstance(mod_date_relative, datetime)
        
        # Test with absolute path
        absolute_path = os.path.abspath(test_file_path)
        mod_date_absolute = get_file_last_modified_date(absolute_path)
        assert isinstance(mod_date_absolute, datetime)
    
    finally:
        # Clean up the test file
        os.remove(test_file_path)