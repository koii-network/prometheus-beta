import os
import pytest
from datetime import datetime
import time

from src.file_last_modified import get_file_last_modified_date

def test_get_file_last_modified_date():
    # Create a temporary file
    test_file_path = 'test_temp_file.txt'
    
    try:
        # Create the file
        with open(test_file_path, 'w') as f:
            f.write('Test content')
        
        # Get the last modified date
        last_modified = get_file_last_modified_date(test_file_path)
        
        # Check if it's a datetime object
        assert isinstance(last_modified, datetime)
        
        # Check if the time is recent (within the last 5 seconds)
        assert (datetime.now() - last_modified).total_seconds() < 5
    
    finally:
        # Clean up the test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

def test_file_not_found():
    # Test for non-existent file
    with pytest.raises(FileNotFoundError):
        get_file_last_modified_date('non_existent_file.txt')

def test_existing_files():
    # Test with existing files in the repository
    test_files = [
        '.gitignore',
        'README.md',
        'requirements.txt'
    ]
    
    for file_path in test_files:
        last_modified = get_file_last_modified_date(file_path)
        assert isinstance(last_modified, datetime)