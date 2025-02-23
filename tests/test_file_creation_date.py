import os
import pytest
import datetime
import tempfile
from src.file_creation_date import get_file_creation_date

def test_get_file_creation_date():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Get the creation date
        creation_date = get_file_creation_date(temp_path)
        
        # Check that it returns a datetime object
        assert isinstance(creation_date, datetime.datetime)
        
        # Check that the creation date is recent (within the last minute)
        assert datetime.datetime.now() - creation_date < datetime.timedelta(minutes=1)
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_file_not_found():
    # Test that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        get_file_creation_date('/path/to/nonexistent/file.txt')

def test_permission_error(mocker):
    # Simulate a permission error
    mock_path = '/some/protected/file.txt'
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.getctime', side_effect=PermissionError)
    
    with pytest.raises(PermissionError):
        get_file_creation_date(mock_path)

def test_function_works_with_existing_file():
    # Create a temporary file and verify function works
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        creation_date = get_file_creation_date(temp_path)
        assert creation_date is not None
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)