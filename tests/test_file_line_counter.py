import os
import pytest
from src.file_line_counter import count_file_lines

def test_count_file_lines_valid_file(tmp_path):
    # Create a temporary file with known number of lines
    test_file = tmp_path / "test_lines.txt"
    test_file.write_text("Line 1\nLine 2\nLine 3")
    
    assert count_file_lines(str(test_file)) == 3

def test_count_file_lines_empty_file(tmp_path):
    # Test with an empty file
    test_file = tmp_path / "empty_file.txt"
    test_file.write_text("")
    
    assert count_file_lines(str(test_file)) == 0

def test_count_file_lines_with_newline(tmp_path):
    # Test file with an extra newline
    test_file = tmp_path / "newline_file.txt"
    test_file.write_text("Line 1\nLine 2\n")
    
    assert count_file_lines(str(test_file)) == 3

def test_count_file_lines_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        count_file_lines("non_existent_file.txt")

def test_count_file_lines_non_text_file(tmp_path):
    # Create a binary file and test line counting
    test_file = tmp_path / "binary_file.bin"
    with open(test_file, 'wb') as f:
        f.write(b'\x00\x01\x02\n\x03\n\x04')
    
    assert count_file_lines(str(test_file)) == 2