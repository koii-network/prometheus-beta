import os
import pytest
import tempfile
import shutil

from src.directory_file_counter import count_files_in_directory

def test_count_files_in_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        assert count_files_in_directory(temp_dir) == 0

def test_count_files_with_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        open(os.path.join(temp_dir, 'file1.txt'), 'w').close()
        open(os.path.join(temp_dir, 'file2.txt'), 'w').close()
        open(os.path.join(temp_dir, 'file3.txt'), 'w').close()
        
        # Create a subdirectory (should not be counted)
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        
        assert count_files_in_directory(temp_dir) == 3

def test_count_files_raises_file_not_found():
    with pytest.raises(FileNotFoundError):
        count_files_in_directory('/path/that/does/not/exist')

def test_count_files_raises_not_a_directory():
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            count_files_in_directory(temp_file.name)