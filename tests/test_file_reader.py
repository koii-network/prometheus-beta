import os
import pytest
from src.file_reader import read_file_line_by_line

def test_read_file_line_by_line_success(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("First line\nSecond line\nThird line")
    
    # Read the file
    lines = read_file_line_by_line(str(test_file))
    
    # Assert the content
    assert lines == ["First line\n", "Second line\n", "Third line"]
    assert len(lines) == 3

def test_read_file_line_by_line_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Read the empty file
    lines = read_file_line_by_line(str(test_file))
    
    # Assert the content
    assert lines == []

def test_read_file_line_by_line_file_not_found():
    # Try to read a non-existent file
    with pytest.raises(FileNotFoundError):
        read_file_line_by_line("non_existent_file.txt")

def test_read_file_line_by_line_with_newline(tmp_path):
    # Create a file with various newline scenarios
    test_file = tmp_path / "newline_test.txt"
    test_file.write_text("Line with newline\n\nAnother line")
    
    # Read the file
    lines = read_file_line_by_line(str(test_file))
    
    # Assert the content
    assert lines == ["Line with newline\n", "\n", "Another line"]
    assert len(lines) == 3