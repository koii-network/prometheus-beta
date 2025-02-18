import os
import pytest
from src.file_reader import read_file_line_by_line

def test_read_file_line_by_line_success(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Line 1\nLine 2\nLine 3")
    
    # Read the file
    lines = read_file_line_by_line(str(test_file))
    
    # Check the lines
    assert lines == ["Line 1\n", "Line 2\n", "Line 3"]
    assert len(lines) == 3

def test_read_file_line_by_line_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Read the empty file
    lines = read_file_line_by_line(str(test_file))
    
    # Check that the result is an empty list
    assert lines == []

def test_read_file_line_by_line_file_not_found():
    # Attempt to read a non-existent file
    with pytest.raises(FileNotFoundError, match="The file non_existent_file.txt was not found."):
        read_file_line_by_line("non_existent_file.txt")

def test_read_file_line_by_line_preserve_newlines(tmp_path):
    # Create a file with mixed newline styles
    test_file = tmp_path / "newline_test.txt"
    test_file.write_text("Windows line\r\nUnix line\nOld Mac line\r")
    
    # Read the file
    lines = read_file_line_by_line(str(test_file))
    
    # Check that newlines are preserved
    assert lines == ["Windows line\r\n", "Unix line\n", "Old Mac line\r"]