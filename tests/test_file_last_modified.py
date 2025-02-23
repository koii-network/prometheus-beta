import os
import pytest
from datetime import datetime
import time

from src.file_last_modified import get_file_last_modified_date

def test_get_file_last_modified_date():
    # Create a temporary file
    test_file_path = 'tests/test_file.txt'
    
    try:
        # Create the file and write some content
        with open(test_file_path, 'w') as f:
            f.write('Test content')
        
        # Get the last modified date of the file
        last_modified = get_file_last_modified_date(test_file_path)
        
        # Check that it returns a datetime object
        assert isinstance(last_modified, datetime)
        
        # Check that the time is very recent (within last few seconds)
        current_time = datetime.fromtimestamp(time.time())
        assert (current_time - last_modified).total_seconds() < 5
    
    finally:
        # Clean up the test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

def test_file_not_found():
    # Test that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        get_file_last_modified_date('non_existent_file.txt')

def test_file_last_modified_with_existing_file():
    # Use an existing file in the repository for additional testing
    existing_files = [
        'README.md', 
        'requirements.txt', 
        '.gitignore'
    ]
    
    for file_path in existing_files:
        try:
            last_modified = get_file_last_modified_date(file_path)
            
            # Check that it returns a datetime object
            assert isinstance(last_modified, datetime)
        except Exception as e:
            pytest.fail(f"Failed to get last modified date for {file_path}: {e}")