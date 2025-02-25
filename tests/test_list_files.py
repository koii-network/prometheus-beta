import os
import pytest
import tempfile
import shutil

from src.list_files import list_directory_files

def test_list_directory_files_normal_case():
    """Test listing files in a directory with multiple files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        files_to_create = ['file1.txt', 'file2.txt', 'file3.txt']
        for filename in files_to_create:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        # Create a subdirectory to ensure only files are returned
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        
        # Test the function
        result = list_directory_files(temp_dir)
        
        # Check that only files are returned
        assert set(result) == set(files_to_create)
        assert len(result) == 3

def test_list_directory_files_empty_directory():
    """Test listing files in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        result = list_directory_files(temp_dir)
        assert result == []

def test_list_directory_files_non_existent_directory():
    """Test handling of non-existent directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        non_existent_dir = os.path.join(temp_dir, 'non_existent_dir')
        
        with pytest.raises(FileNotFoundError):
            list_directory_files(non_existent_dir)

def test_list_directory_files_not_a_directory():
    """Test handling of a path that is not a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file instead of a directory
        test_file = os.path.join(temp_dir, 'test_file.txt')
        with open(test_file, 'w') as f:
            f.write('test content')
        
        with pytest.raises(NotADirectoryError):
            list_directory_files(test_file)