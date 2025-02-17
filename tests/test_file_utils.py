import os
import pytest
import tempfile
import time
from src.file_utils import find_most_recent_file

def test_find_most_recent_file():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files with different modification times
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        file3_path = os.path.join(temp_dir, 'file3.txt')
        
        # Create files with staggered modification times
        with open(file1_path, 'w') as f:
            f.write('file1 content')
        time.sleep(0.1)  # Small delay to ensure different modification times
        
        with open(file2_path, 'w') as f:
            f.write('file2 content')
        time.sleep(0.1)
        
        with open(file3_path, 'w') as f:
            f.write('file3 content')
        
        # Find the most recently modified file
        most_recent = find_most_recent_file(temp_dir)
        
        # Verify the most recent file is file3
        assert most_recent == file3_path

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Verify None is returned for an empty directory
        assert find_most_recent_file(temp_dir) is None

def test_invalid_directory():
    # Verify ValueError is raised for invalid directory
    with pytest.raises(ValueError, match="The specified path is not a valid directory"):
        find_most_recent_file('/path/that/does/not/exist')

def test_current_directory():
    # Test using current directory
    current_dir_result = find_most_recent_file('.')
    assert current_dir_result is not None
    assert os.path.isfile(current_dir_result)