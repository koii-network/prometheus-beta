import os
import pytest
import time
from src.file_creation_date import get_file_creation_date

def test_get_file_creation_date_existing_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Get creation time
    creation_time = get_file_creation_date(str(test_file))
    
    # Check that creation time is a valid timestamp and is recent
    assert isinstance(creation_time, float)
    assert abs(time.time() - creation_time) < 10  # Within 10 seconds of current time

def test_get_file_creation_date_nonexistent_file():
    # Test for FileNotFoundError when file doesn't exist
    with pytest.raises(FileNotFoundError):
        get_file_creation_date("nonexistent_file.txt")

def test_get_file_creation_date_existing_project_file():
    # Test with an existing file in the project
    existing_files = [
        '.gitignore',
        'README.md',
        'requirements.txt'
    ]
    
    for file in existing_files:
        try:
            creation_time = get_file_creation_date(file)
            assert isinstance(creation_time, float)
        except Exception as e:
            pytest.fail(f"Failed to get creation time for {file}: {str(e)}")