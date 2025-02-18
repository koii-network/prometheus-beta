import os
import pytest
from src.file_compare import are_files_identical

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
    file2.write_text("Hello, universe!")
    
    assert are_files_identical(str(file1), str(file2)) == False

def test_empty_files(tmp_path):
    # Create two empty files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    
    file1.touch()
    file2.touch()
    
    assert are_files_identical(str(file1), str(file2)) == True

def test_large_files(tmp_path):
    # Create large identical files
    file1 = tmp_path / "large1.txt"
    file2 = tmp_path / "large2.txt"
    
    large_content = "A" * 1024 * 1024  # 1 MB of content
    file1.write_text(large_content)
    file2.write_text(large_content)
    
    assert are_files_identical(str(file1), str(file2)) == True

def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        are_files_identical("nonexistent1.txt", "nonexistent2.txt")

def test_is_directory(tmp_path):
    # Create a directory
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    
    with pytest.raises(IsADirectoryError):
        are_files_identical(str(dir_path), str(dir_path))