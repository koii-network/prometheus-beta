import os
import pytest
from src.file_line_counter import count_file_lines

def test_count_lines_normal_file(tmp_path):
    """Test counting lines in a normal text file."""
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Line 1\nLine 2\nLine 3")
    
    assert count_file_lines(str(test_file)) == 3

def test_count_lines_empty_file(tmp_path):
    """Test counting lines in an empty file."""
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    assert count_file_lines(str(test_file)) == 0

def test_count_lines_with_blank_lines(tmp_path):
    """Test counting lines including blank lines."""
    test_file = tmp_path / "blank_lines_file.txt"
    test_file.write_text("Line 1\n\nLine 3\n\n")
    
    assert count_file_lines(str(test_file)) == 4

def test_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError, match="does not exist"):
        count_file_lines("non_existent_file.txt")

def test_file_with_different_line_endings(tmp_path):
    """Test file with different line endings."""
    test_file = tmp_path / "mixed_endings.txt"
    test_file.write_text("Line 1\rLine 2\r\nLine 3\n")
    
    assert count_file_lines(str(test_file)) == 3

def test_large_file(tmp_path):
    """Test file with multiple lines."""
    test_file = tmp_path / "large_file.txt"
    lines = [f"Line {i}" for i in range(1000)]
    test_file.write_text("\n".join(lines))
    
    assert count_file_lines(str(test_file)) == 1000