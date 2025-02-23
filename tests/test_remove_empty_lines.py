import os
import pytest
from src.remove_empty_lines import remove_empty_lines

@pytest.fixture
def sample_file(tmp_path):
    """Create a temporary file with mixed empty and non-empty lines."""
    file_path = tmp_path / "sample.txt"
    with open(file_path, 'w') as f:
        f.write("Hello\n\nWorld\n\n\nPython\n")
    return file_path

def test_remove_empty_lines_inplace(sample_file):
    """Test removing empty lines in-place."""
    empty_count = remove_empty_lines(str(sample_file))
    
    assert empty_count == 3
    
    with open(sample_file, 'r') as f:
        lines = f.readlines()
    
    assert lines == ["Hello\n", "World\n", "Python\n"]

def test_remove_empty_lines_to_new_file(sample_file, tmp_path):
    """Test removing empty lines to a new file."""
    output_file = tmp_path / "output.txt"
    empty_count = remove_empty_lines(str(sample_file), str(output_file))
    
    assert empty_count == 3
    
    with open(output_file, 'r') as f:
        lines = f.readlines()
    
    assert lines == ["Hello\n", "World\n", "Python\n"]

def test_file_with_no_empty_lines(tmp_path):
    """Test a file with no empty lines."""
    file_path = tmp_path / "no_empty.txt"
    with open(file_path, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    
    empty_count = remove_empty_lines(str(file_path))
    
    assert empty_count == 0
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    assert lines == ["Line 1\n", "Line 2\n", "Line 3\n"]

def test_empty_file(tmp_path):
    """Test an entirely empty file."""
    file_path = tmp_path / "empty.txt"
    with open(file_path, 'w') as f:
        f.write("\n\n\n")
    
    empty_count = remove_empty_lines(str(file_path))
    
    assert empty_count == 3
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    assert lines == []

def test_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        remove_empty_lines("non_existent_file.txt")