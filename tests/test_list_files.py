import os
import pytest
import tempfile
import shutil

from src.list_files import list_directory_files

def test_list_directory_files_basic():
    """Test listing files in a temporary directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        test_files = ['file1.txt', 'file2.txt', 'file3.txt']
        for filename in test_files:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        # List files and verify
        listed_files = list_directory_files(temp_dir)
        assert set(listed_files) == set(test_files)

def test_list_directory_files_empty():
    """Test listing files in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        listed_files = list_directory_files(temp_dir)
        assert listed_files == []

def test_list_directory_files_includes_only_files():
    """Verify that only files are returned, not subdirectories."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files and a subdirectory
        test_files = ['file1.txt', 'file2.txt']
        for filename in test_files:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        # Create a subdirectory
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        
        # List files and verify
        listed_files = list_directory_files(temp_dir)
        assert set(listed_files) == set(test_files)

def test_list_directory_files_nonexistent_directory():
    """Test that FileNotFoundError is raised for nonexistent directory."""
    with tempfile.TemporaryDirectory() as parent_dir:
        nonexistent_dir = os.path.join(parent_dir, 'nonexistent_dir')
        
        with pytest.raises(FileNotFoundError):
            list_directory_files(nonexistent_dir)

def test_list_directory_files_not_a_directory():
    """Test that NotADirectoryError is raised when path is not a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file to use as an invalid directory path
        test_file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('test content')
        
        with pytest.raises(NotADirectoryError):
            list_directory_files(test_file_path)