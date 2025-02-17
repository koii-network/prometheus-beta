import os
import pytest
import tempfile
import shutil

from src.directory_file_counter import count_files_in_directory

def test_count_files_in_directory():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('test')
        with open(os.path.join(temp_dir, 'file2.txt'), 'w') as f:
            f.write('test')
        with open(os.path.join(temp_dir, 'file3.txt'), 'w') as f:
            f.write('test')
        
        # Also create a subdirectory to ensure it's not counted
        os.mkdir(os.path.join(temp_dir, 'subdirectory'))
        
        # Test file counting
        assert count_files_in_directory(temp_dir) == 3

def test_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        assert count_files_in_directory(temp_dir) == 0

def test_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        count_files_in_directory('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            count_files_in_directory(temp_file.name)