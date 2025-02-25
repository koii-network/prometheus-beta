import os
import pytest
from src.file_reader import read_file_line_by_line

def test_read_file_line_by_line_normal():
    # Create a temporary test file
    with open('tests/test_file.txt', 'w') as f:
        f.write("Hello\nWorld\nPython")
    
    # Test reading the file
    lines = read_file_line_by_line('tests/test_file.txt')
    assert lines == ['Hello', 'World', 'Python']
    
    # Clean up the test file
    os.remove('tests/test_file.txt')

def test_read_file_line_by_line_empty_file():
    # Create an empty test file
    with open('tests/empty_file.txt', 'w') as f:
        pass
    
    # Test reading an empty file
    lines = read_file_line_by_line('tests/empty_file.txt')
    assert lines == []
    
    # Clean up the test file
    os.remove('tests/empty_file.txt')

def test_read_file_line_by_line_nonexistent_file():
    # Test reading a nonexistent file
    with pytest.raises(FileNotFoundError):
        read_file_line_by_line('tests/nonexistent_file.txt')

def test_read_file_line_by_line_with_newline_variations():
    # Create a test file with different newline styles
    with open('tests/newline_file.txt', 'w') as f:
        f.write("Line1\rLine2\nLine3\r\nLine4")
    
    # Test reading the file
    lines = read_file_line_by_line('tests/newline_file.txt')
    assert lines == ['Line1', 'Line2', 'Line3', 'Line4']
    
    # Clean up the test file
    os.remove('tests/newline_file.txt')