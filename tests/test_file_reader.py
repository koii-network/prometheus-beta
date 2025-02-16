import os
import pytest
from src.file_reader import read_file_line_by_line

def test_read_file_line_by_line_success(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Line 1\nLine 2\nLine 3")
    
    # Read the file
    lines = read_file_line_by_line(str(test_file))
    
    # Assert the contents
    assert lines == ["Line 1\n", "Line 2\n", "Line 3"]

def test_read_file_line_by_line_empty_file(tmp_path):
    # Create an empty test file
    test_file = tmp_path / "empty_file.txt"
    test_file.write_text("")
    
    # Read the file
    lines = read_file_line_by_line(str(test_file))
    
    # Assert the contents
    assert lines == []

def test_read_file_line_by_line_file_not_found():
    # Test raising FileNotFoundError for non-existent file
    with pytest.raises(FileNotFoundError):
        read_file_line_by_line("non_existent_file.txt")

def test_read_file_line_by_line_multiple_lines(tmp_path):
    # Create a test file with multiple lines
    test_file = tmp_path / "multi_line_file.txt"
    test_file.write_text("First line\nSecond line\nThird line\nFourth line")
    
    # Read the file
    lines = read_file_line_by_line(str(test_file))
    
    # Assert the contents
    assert len(lines) == 4
    assert lines[0] == "First line\n"
    assert lines[3] == "Fourth line"