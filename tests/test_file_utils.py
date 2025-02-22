import os
import pytest
from datetime import datetime
import time

from src.file_utils import get_last_modified_date

def test_get_last_modified_date():
    # Create a temporary file
    test_file_path = 'tests/test_file.txt'
    
    # Write some content to the file
    with open(test_file_path, 'w') as f:
        f.write('Test content')
    
    try:
        # Get the last modified date
        modified_date = get_last_modified_date(test_file_path)
        
        # Check that it's a datetime object
        assert isinstance(modified_date, datetime)
        
        # Check that the modified date is very recent (within last 5 seconds)
        assert (datetime.now() - modified_date).total_seconds() < 5
    
    finally:
        # Clean up the test file
        os.remove(test_file_path)

def test_get_last_modified_date_nonexistent_file():
    # Test for FileNotFoundError
    with pytest.raises(FileNotFoundError):
        get_last_modified_date('nonexistent_file.txt')

def test_get_last_modified_date_with_existing_files():
    # Test with existing files in the repository
    test_files = [
        '.gitignore',
        'README.md',
        'requirements.txt'
    ]
    
    for file in test_files:
        # Attempt to get last modified date for each file
        modified_date = get_last_modified_date(file)
        
        # Verify it returns a datetime
        assert isinstance(modified_date, datetime)
        
        # Verify the date is not in the future
        assert modified_date <= datetime.now()