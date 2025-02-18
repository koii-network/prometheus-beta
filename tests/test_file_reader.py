import os
import pytest
from src.file_reader import read_file_line_by_line

def test_read_file_line_by_line():
    # Create a temporary test file
    test_file_path = 'tests/test_file.txt'
    test_content = ["Hello, world!\n", "This is a test file.\n", "Line 3 of the test."]
    
    # Write test content to the file
    with open(test_file_path, 'w') as f:
        f.writelines(test_content)
    
    try:
        # Test reading the file
        result = read_file_line_by_line(test_file_path)
        
        # Assert the lines match the original content
        assert result == test_content, "File content does not match expected lines"
    
    finally:
        # Clean up the test file
        os.remove(test_file_path)

def test_read_nonexistent_file():
    # Test reading a file that does not exist
    with pytest.raises(FileNotFoundError, match="The file non_existent_file.txt was not found."):
        read_file_line_by_line('non_existent_file.txt')

def test_empty_file():
    # Create an empty test file
    test_file_path = 'tests/empty_test_file.txt'
    
    try:
        # Create an empty file
        open(test_file_path, 'w').close()
        
        # Test reading the empty file
        result = read_file_line_by_line(test_file_path)
        
        # Assert the result is an empty list
        assert result == [], "Empty file should return an empty list"
    
    finally:
        # Clean up the test file
        os.remove(test_file_path)