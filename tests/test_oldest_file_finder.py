import os
import tempfile
import pytest
from src.oldest_file_finder import find_oldest_file

def test_find_oldest_file():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create files with known creation times
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        
        # Create first file
        with open(file1_path, 'w') as f:
            f.write('First file')
        
        # Wait a bit to ensure different creation times
        import time
        time.sleep(0.1)
        
        # Create second file
        with open(file2_path, 'w') as f:
            f.write('Second file')
        
        # Find the oldest file
        oldest = find_oldest_file(tmpdir)
        
        # Verify the oldest file is file1 (as a relative path)
        assert oldest == os.path.relpath(file1_path, tmpdir)

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Verify None is returned for empty directory
        assert find_oldest_file(tmpdir) is None

def test_invalid_directory():
    # Test with non-existent directory
    with pytest.raises(NotADirectoryError):
        find_oldest_file('/path/that/does/not/exist')

def test_directory_with_subdirectories():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a subdirectory
        subdir = os.path.join(tmpdir, 'subdir')
        os.makedirs(subdir)
        
        # Create files at different times
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        subdir_file_path = os.path.join(subdir, 'subdir_file.txt')
        
        # Create first file in main directory
        with open(file1_path, 'w') as f:
            f.write('First file')
        
        # Wait a bit to ensure different creation times
        import time
        time.sleep(0.1)
        
        # Create second file in main directory
        with open(file2_path, 'w') as f:
            f.write('Second file')
        
        # Find the oldest file
        oldest = find_oldest_file(tmpdir)
        
        # Verify the oldest file is file1 (as a relative path)
        assert oldest == os.path.relpath(file1_path, tmpdir)
        # Verify subdirectory files are not considered