import os
import pytest
import time
import tempfile
from src.recent_file_finder import find_most_recent_file


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname


def test_find_most_recent_file_basic(temp_dir):
    """Test finding the most recently modified file in a directory."""
    # Create multiple files with different modification times
    file1_path = os.path.join(temp_dir, 'file1.txt')
    file2_path = os.path.join(temp_dir, 'file2.txt')
    
    # Create first file
    with open(file1_path, 'w') as f:
        f.write('content1')
    
    # Wait a bit to ensure different modification times
    time.sleep(0.1)
    
    # Create second file
    with open(file2_path, 'w') as f:
        f.write('content2')
    
    # Find most recent file
    most_recent = find_most_recent_file(temp_dir)
    
    # Assert the most recent file is the last created file
    assert most_recent == file2_path


def test_empty_directory(temp_dir):
    """Test behavior with an empty directory."""
    result = find_most_recent_file(temp_dir)
    assert result is None


def test_invalid_directory():
    """Test that an invalid directory raises an appropriate error."""
    with pytest.raises(NotADirectoryError):
        find_most_recent_file('/path/that/does/not/exist')


def test_invalid_input_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError):
        find_most_recent_file(123)  # Non-string/path-like input


def test_only_one_file(temp_dir):
    """Test finding the most recent file when only one file exists."""
    file_path = os.path.join(temp_dir, 'single_file.txt')
    
    with open(file_path, 'w') as f:
        f.write('content')
    
    most_recent = find_most_recent_file(temp_dir)
    assert most_recent == file_path