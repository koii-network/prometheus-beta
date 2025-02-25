import os
import pytest
import datetime
from src.file_utils import get_file_creation_date

def test_get_file_creation_date():
    # Create a temporary file
    test_file_path = 'tests/test_file.txt'
    
    try:
        # Create a test file
        with open(test_file_path, 'w') as f:
            f.write('Test content')
        
        # Get the file creation date
        creation_date = get_file_creation_date(test_file_path)
        
        # Check that it returns a datetime object
        assert isinstance(creation_date, datetime.datetime)
        
        # Check that the creation date is recent (within the last minute)
        assert datetime.datetime.now() - creation_date < datetime.timedelta(minutes=1)
    
    finally:
        # Clean up the test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

def test_file_not_found():
    # Test that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        get_file_creation_date('non_existent_file.txt')

def test_file_creation_date_type():
    # Create a temporary file
    test_file_path = 'tests/test_file_type.txt'
    
    try:
        # Create a test file
        with open(test_file_path, 'w') as f:
            f.write('Type check')
        
        # Get the file creation date
        creation_date = get_file_creation_date(test_file_path)
        
        # Verify that the returned value is a datetime object
        assert isinstance(creation_date, datetime.datetime)
    
    finally:
        # Clean up the test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

def test_user_path_expansion():
    # Create a temporary file in user's home directory
    test_file_path = os.path.expanduser('~/test_expansion.txt')
    
    try:
        # Create a test file
        with open(test_file_path, 'w') as f:
            f.write('Path expansion test')
        
        # Get the file creation date using ~ path
        creation_date = get_file_creation_date('~/test_expansion.txt')
        
        # Check that it returns a datetime object
        assert isinstance(creation_date, datetime.datetime)
    
    finally:
        # Clean up the test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)