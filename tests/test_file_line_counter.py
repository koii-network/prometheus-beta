import os
import pytest
from src.file_line_counter import count_file_lines

def test_count_file_lines_existing_file(tmp_path):
    # Create a temporary file with known number of lines
    test_file = tmp_path / "test_lines.txt"
    test_file.write_text("Line 1\nLine 2\nLine 3")
    
    assert count_file_lines(str(test_file)) == 3

def test_count_file_lines_empty_file(tmp_path):
    # Test empty file
    test_file = tmp_path / "empty.txt"
    test_file.touch()
    
    assert count_file_lines(str(test_file)) == 0

def test_count_file_lines_nonexistent_file():
    # Test file not found
    with pytest.raises(FileNotFoundError):
        count_file_lines("nonexistent_file.txt")

def test_count_file_lines_multiple_newlines(tmp_path):
    # Test file with multiple newlines
    test_file = tmp_path / "multiple_newlines.txt"
    test_file.write_text("Line 1\n\n\nLine 2\n")
    
    assert count_file_lines(str(test_file)) == 5