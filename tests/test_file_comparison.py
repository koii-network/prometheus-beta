import os
import pytest
from src.file_comparison import are_files_identical

def test_identical_files(tmp_path):
    # Create two identical files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.write_text("Hello, world!")
    file2.write_text("Hello, world!")
    
    assert are_files_identical(str(file1), str(file2)) == True

def test_different_files(tmp_path):
    # Create two different files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.write_text("Hello, world!")
    file2.write_text("Different content")
    
    assert are_files_identical(str(file1), str(file2)) == False

def test_empty_files(tmp_path):
    # Create two empty files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.touch()
    file2.touch()
    
    assert are_files_identical(str(file1), str(file2)) == True

def test_file_not_found():
    # Test non-existent files
    with pytest.raises(FileNotFoundError):
        are_files_identical("non_existent_file1.txt", "non_existent_file2.txt")

def test_is_directory(tmp_path):
    # Test directory paths
    with pytest.raises(IsADirectoryError):
        are_files_identical(str(tmp_path), str(tmp_path / "subdir"))