import os
import pytest
import tempfile
import time
from src.oldest_file_finder import find_oldest_file


def test_find_oldest_file_basic():
    """Test finding the oldest file in a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files with different creation times
        file1 = os.path.join(temp_dir, 'file1.txt')
        file2 = os.path.join(temp_dir, 'file2.txt')
        
        # Ensure files are created at different times
        with open(file1, 'w') as f:
            f.write('Test file 1')
        time.sleep(0.1)  # Small delay to ensure different creation times
        with open(file2, 'w') as f:
            f.write('Test file 2')
        
        # Find the oldest file
        oldest = find_oldest_file(temp_dir)
        
        # Verify the oldest file is the first created file
        assert oldest == file1


def test_find_oldest_file_empty_directory():
    """Test behavior with an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Should return None for an empty directory
        assert find_oldest_file(temp_dir) is None


def test_find_oldest_file_nonexistent_directory():
    """Test error handling for nonexistent directory."""
    with pytest.raises(FileNotFoundError):
        find_oldest_file('/path/to/nonexistent/directory')


def test_find_oldest_file_not_a_directory():
    """Test error handling when path is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            find_oldest_file(temp_file.name)


def test_find_oldest_file_multiple_files():
    """Test finding the oldest file with multiple files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create multiple files at different times
        files = []
        for i in range(5):
            file_path = os.path.join(temp_dir, f'file{i}.txt')
            with open(file_path, 'w') as f:
                f.write(f'Test content {i}')
            time.sleep(0.1)  # Ensure different creation times
            files.append(file_path)
        
        # Find the oldest file
        oldest = find_oldest_file(temp_dir)
        
        # Verify the oldest file is the first created file
        assert oldest == files[0]