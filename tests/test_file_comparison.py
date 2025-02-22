import os
import pytest
from src.file_comparison import are_files_identical

def test_identical_files(tmp_path):
    # Create two identical files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    
    file1.write_text("This is a test file")
    file2.write_text("This is a test file")
    
    assert are_files_identical(str(file1), str(file2)) == True

def test_different_files(tmp_path):
    # Create two different files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    
    file1.write_text("This is file 1")
    file2.write_text("This is file 2")
    
    assert are_files_identical(str(file1), str(file2)) == False

def test_different_file_sizes(tmp_path):
    # Create files with different sizes
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    
    file1.write_text("Short text")
    file2.write_text("Longer text that is different")
    
    assert are_files_identical(str(file1), str(file2)) == False

def test_non_existent_file(tmp_path):
    # Test file not found scenario
    file1 = tmp_path / "file1.txt"
    non_existent_file = tmp_path / "non_existent.txt"
    
    file1.write_text("Some content")
    
    with pytest.raises(FileNotFoundError):
        are_files_identical(str(file1), str(non_existent_file))
    
    with pytest.raises(FileNotFoundError):
        are_files_identical(str(non_existent_file), str(file1))

def test_empty_files(tmp_path):
    # Test identical empty files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    
    file1.write_text("")
    file2.write_text("")
    
    assert are_files_identical(str(file1), str(file2)) == True