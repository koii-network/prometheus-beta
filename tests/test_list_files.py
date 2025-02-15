import os
import pytest
import tempfile
import shutil

from src.list_files import list_files

def test_list_files_current_directory():
    """Test listing files in the current directory."""
    files = list_files()
    assert isinstance(files, list)
    # Verify expected files exist in the current directory
    expected_files = ['.gitignore', 'README.md', 'requirements.txt']
    for expected_file in expected_files:
        assert expected_file in files

def test_list_files_with_specified_directory():
    """Test listing files in a specified directory."""
    # Create a temporary directory with some test files
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Create some test files
        test_files = ['file1.txt', 'file2.txt', 'file3.txt']
        for filename in test_files:
            with open(os.path.join(tmpdirname, filename), 'w') as f:
                f.write('test content')
        
        # Test listing files
        result = list_files(tmpdirname)
        assert set(result) == set(test_files)

def test_list_files_with_nonexistent_directory():
    """Test that an error is raised for a nonexistent directory."""
    with pytest.raises(FileNotFoundError):
        list_files('/path/to/nonexistent/directory')

def test_list_files_with_file_instead_of_directory():
    """Test that an error is raised when a file is provided instead of a directory."""
    with pytest.raises(NotADirectoryError):
        list_files('.gitignore')

def test_list_files_empty_directory():
    """Test listing files in an empty directory."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        result = list_files(tmpdirname)
        assert result == []