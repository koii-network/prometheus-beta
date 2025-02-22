import os
import pytest
import tempfile
import shutil

from src.directory_file_counter import count_files_in_directory

def test_count_files_in_current_directory():
    # Create a temporary directory with some test files
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Create some test files
        test_files = ['file1.txt', 'file2.txt', 'file3.txt']
        for filename in test_files:
            with open(os.path.join(tmpdirname, filename), 'w') as f:
                f.write('test content')
        
        # Create a subdirectory to ensure only files are counted
        os.mkdir(os.path.join(tmpdirname, 'subdirectory'))
        
        # Change current working directory to temp directory
        original_cwd = os.getcwd()
        os.chdir(tmpdirname)
        
        try:
            # Test the function
            file_count = count_files_in_directory('.')
            assert file_count == 3
        finally:
            # Change back to original directory
            os.chdir(original_cwd)

def test_count_files_in_specific_directory():
    # Create a temporary directory with some test files
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Create some test files
        test_files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
        for filename in test_files:
            with open(os.path.join(tmpdirname, filename), 'w') as f:
                f.write('test content')
        
        # Create a subdirectory to ensure only files are counted
        os.mkdir(os.path.join(tmpdirname, 'subdirectory'))
        
        # Test the function
        file_count = count_files_in_directory(tmpdirname)
        assert file_count == 4

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_count = count_files_in_directory(tmpdirname)
        assert file_count == 0

def test_nonexistent_directory():
    # Test for FileNotFoundError
    with pytest.raises(FileNotFoundError):
        count_files_in_directory('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        try:
            # Test for NotADirectoryError
            with pytest.raises(NotADirectoryError):
                count_files_in_directory(tmpfile.name)
        finally:
            # Clean up the temporary file
            os.unlink(tmpfile.name)