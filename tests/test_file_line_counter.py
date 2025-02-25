import os
import pytest
from src.file_line_counter import count_file_lines

def test_count_lines_normal_file(tmp_path):
    """Test counting lines in a normal text file."""
    test_file = tmp_path / "sample.txt"
    test_file.write_text("Line 1\nLine 2\nLine 3")
    
    assert count_file_lines(str(test_file)) == 3

def test_count_lines_empty_file(tmp_path):
    """Test counting lines in an empty file."""
    test_file = tmp_path / "empty.txt"
    test_file.write_text("")
    
    assert count_file_lines(str(test_file)) == 0

def test_count_lines_file_with_newline(tmp_path):
    """Test counting lines in a file with a trailing newline."""
    test_file = tmp_path / "newline.txt"
    test_file.write_text("Line 1\nLine 2\n")
    
    assert count_file_lines(str(test_file)) == 2

def test_count_lines_file_not_found():
    """Test handling of file not found."""
    with pytest.raises(FileNotFoundError):
        count_file_lines("non_existent_file.txt")

def test_count_lines_permission_error(tmp_path):
    """Test handling of permission-related file access errors."""
    test_file = tmp_path / "no_read_file.txt"
    test_file.write_text("Some content")
    
    # Make the file unreadable
    test_file.chmod(0o000)
    
    with pytest.raises(IOError):
        count_file_lines(str(test_file))