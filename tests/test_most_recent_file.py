import os
import pytest
import tempfile
import time
from src.most_recent_file import find_most_recent_file

def test_find_most_recent_file():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create some test files with different modification times
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        file3_path = os.path.join(tmpdir, 'file3.txt')
        
        # Create files
        with open(file1_path, 'w') as f:
            f.write('file1 content')
        
        # Wait a bit to ensure different modification times
        time.sleep(0.1)
        
        with open(file2_path, 'w') as f:
            f.write('file2 content')
        
        time.sleep(0.1)
        
        with open(file3_path, 'w') as f:
            f.write('file3 content')
        
        # Find the most recent file
        most_recent = find_most_recent_file(tmpdir)
        
        # Verify it's the last created file
        assert most_recent == file3_path

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Should return None for an empty directory
        assert find_most_recent_file(tmpdir) is None

def test_invalid_directory():
    # Try with a non-existent directory
    with pytest.raises(ValueError, match="The specified path is not a directory"):
        find_most_recent_file('/path/that/does/not/exist')

def test_default_directory():
    # Test with default current directory
    # This is a basic check to ensure it doesn't raise an error
    result = find_most_recent_file()
    # While we can't predict the exact file, it should be a string path or None
    assert result is None or isinstance(result, str)