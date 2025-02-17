import os
import pytest
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.directory_files import list_directory_files

def test_list_directory_files(tmp_path):
    # Create some test files
    test_files = ['file1.txt', 'file2.txt', 'file3.log']
    for filename in test_files:
        (tmp_path / filename).write_text('test content')
    
    # Create a subdirectory to ensure only files are returned
    (tmp_path / 'subdir').mkdir()
    
    # Test listing files
    files = list_directory_files(str(tmp_path))
    assert files == sorted(test_files)
    assert len(files) == 3

def test_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        list_directory_files('/path/to/nonexistent/directory')

def test_not_a_directory(tmp_path):
    # Create a file instead of a directory
    test_file = tmp_path / 'not_a_dir.txt'
    test_file.write_text('test')
    
    with pytest.raises(NotADirectoryError):
        list_directory_files(str(test_file))

def test_empty_directory(tmp_path):
    # Test an empty directory
    files = list_directory_files(str(tmp_path))
    assert files == []

def test_current_directory():
    # Ensure function works with current directory
    current_dir_files = list_directory_files('.')
    assert isinstance(current_dir_files, list)
    # Check for known files in the repository
    assert '.gitignore' in current_dir_files
    assert 'README.md' in current_dir_files
    assert 'requirements.txt' in current_dir_files