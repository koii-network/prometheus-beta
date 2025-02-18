import os
import pytest
from src.file_comparison import are_files_identical

@pytest.fixture
def create_test_files(tmp_path):
    """Create temporary test files for comparison"""
    # File 1: Identical content
    file1 = tmp_path / "file1.txt"
    file1.write_text("Hello, world!")
    
    # File 2: Identical content
    file2 = tmp_path / "file2.txt"
    file2.write_text("Hello, world!")
    
    # Different content file
    file3 = tmp_path / "file3.txt"
    file3.write_text("Different content")
    
    return file1, file2, file3

def test_identical_files(create_test_files):
    """Test that identical files return True"""
    file1, file2, _ = create_test_files
    assert are_files_identical(str(file1), str(file2)) == True

def test_different_files(create_test_files):
    """Test that different files return False"""
    file1, _, file3 = create_test_files
    assert are_files_identical(str(file1), str(file3)) == False

def test_file_not_found():
    """Test that FileNotFoundError is raised for non-existent files"""
    with pytest.raises(FileNotFoundError):
        are_files_identical("non_existent_file1.txt", "non_existent_file2.txt")

def test_empty_files(tmp_path):
    """Test comparison of empty files"""
    empty_file1 = tmp_path / "empty1.txt"
    empty_file1.touch()
    
    empty_file2 = tmp_path / "empty2.txt"
    empty_file2.touch()
    
    assert are_files_identical(str(empty_file1), str(empty_file2)) == True

def test_large_file_comparison(tmp_path):
    """Test comparison of large files"""
    large_file1 = tmp_path / "large1.txt"
    large_file1.write_text("A" * 1_000_000)
    
    large_file2 = tmp_path / "large2.txt"
    large_file2.write_text("A" * 1_000_000)
    
    large_file3 = tmp_path / "large3.txt"
    large_file3.write_text("A" * 999_999 + "B")
    
    assert are_files_identical(str(large_file1), str(large_file2)) == True
    assert are_files_identical(str(large_file1), str(large_file3)) == False