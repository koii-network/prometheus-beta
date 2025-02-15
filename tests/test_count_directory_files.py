import os
import pytest
import tempfile
from src.count_directory_files import count_directory_files

def test_count_directory_files_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        assert count_directory_files(temp_dir) == 0

def test_count_directory_files_with_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        open(os.path.join(temp_dir, 'file1.txt'), 'w').close()
        open(os.path.join(temp_dir, 'file2.txt'), 'w').close()
        open(os.path.join(temp_dir, 'file3.txt'), 'w').close()
        
        assert count_directory_files(temp_dir) == 3

def test_count_directory_files_mixed_content():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files and a subdirectory
        open(os.path.join(temp_dir, 'file1.txt'), 'w').close()
        open(os.path.join(temp_dir, 'file2.txt'), 'w').close()
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        
        assert count_directory_files(temp_dir) == 2

def test_count_directory_files_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        count_directory_files('/path/to/nonexistent/directory')

def test_count_directory_files_not_a_directory():
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            count_directory_files(temp_file.name)