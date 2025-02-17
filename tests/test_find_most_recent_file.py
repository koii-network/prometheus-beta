import os
import pytest
import time
from src.find_most_recent_file import find_most_recent_file

@pytest.fixture
def temp_dir(tmpdir):
    """Create a temporary directory with some test files."""
    # Create test files with different modification times
    f1 = tmpdir.join("file1.txt")
    f1.write("content1")
    time.sleep(0.1)  # Ensure different modification times
    
    f2 = tmpdir.join("file2.txt")
    f2.write("content2")
    time.sleep(0.1)
    
    f3 = tmpdir.join("file3.txt")
    f3.write("content3")
    
    return tmpdir

def test_find_most_recent_file(temp_dir):
    """Test finding the most recently modified file."""
    most_recent = find_most_recent_file(str(temp_dir))
    
    # The most recently modified file will be file3.txt
    assert os.path.basename(most_recent) == "file3.txt"

def test_find_most_recent_file_empty_dir(tmpdir):
    """Test behavior with an empty directory."""
    result = find_most_recent_file(str(tmpdir))
    assert result is None

def test_nonexistent_directory():
    """Test that an error is raised for a nonexistent directory."""
    with pytest.raises(FileNotFoundError):
        find_most_recent_file("/path/that/does/not/exist")

def test_not_a_directory():
    """Test that an error is raised when the path is not a directory."""
    with pytest.raises(NotADirectoryError):
        find_most_recent_file("README.md")  # Assuming README.md exists in the project root

def test_returns_full_file_path(temp_dir):
    """Verify that the function returns the full file path."""
    most_recent = find_most_recent_file(str(temp_dir))
    assert os.path.isabs(most_recent)
    assert os.path.exists(most_recent)