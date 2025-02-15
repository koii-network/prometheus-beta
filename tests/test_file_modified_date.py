import os
import pytest
from datetime import datetime, timedelta
from src.file_modified_date import get_file_last_modified

def test_get_file_last_modified_existing_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Get the last modified date
    modified_date = get_file_last_modified(str(test_file))
    
    # Check that it returns a datetime object
    assert isinstance(modified_date, datetime)
    
    # Check that the modified date is very recent (within last few seconds)
    assert datetime.now() - modified_date < timedelta(seconds=5)

def test_get_file_last_modified_nonexistent_file():
    # Test that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        get_file_last_modified("non_existent_file.txt")

def test_get_file_last_modified_with_specific_files():
    # Test with specific files in the repository
    test_files = [
        ".gitignore",
        "README.md", 
        "requirements.txt"
    ]
    
    for file in test_files:
        # Ensure file exists
        assert os.path.exists(file), f"File {file} does not exist"
        
        # Get last modified date
        modified_date = get_file_last_modified(file)
        
        # Check that it returns a datetime object
        assert isinstance(modified_date, datetime)
        
        # Check that the modified date is not in the future
        assert modified_date <= datetime.now()