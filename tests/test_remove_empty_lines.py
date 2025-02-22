import os
import pytest
from src.remove_empty_lines import remove_empty_lines

def test_remove_empty_lines(tmp_path):
    # Create a test input file with mixed empty and non-empty lines
    test_input = tmp_path / "input.txt"
    test_input.write_text("Hello\n\nWorld\n   \nPython\n\n")
    
    # Call the function
    empty_lines_count = remove_empty_lines(str(test_input))
    
    # Check contents of the file
    with open(test_input, 'r') as f:
        lines = f.readlines()
    
    # Verify expected results
    assert empty_lines_count == 3
    assert lines == ["Hello\n", "World\n", "Python\n"]

def test_remove_empty_lines_different_output(tmp_path):
    # Test with a separate output file
    test_input = tmp_path / "input.txt"
    test_output = tmp_path / "output.txt"
    test_input.write_text("Data1\n\nData2\n")
    
    # Call the function with output file
    empty_lines_count = remove_empty_lines(str(test_input), str(test_output))
    
    # Verify source file unchanged
    with open(test_input, 'r') as f:
        original_lines = f.readlines()
    assert original_lines == ["Data1\n", "\n", "Data2\n"]
    
    # Verify output file
    with open(test_output, 'r') as f:
        output_lines = f.readlines()
    
    assert empty_lines_count == 1
    assert output_lines == ["Data1\n", "Data2\n"]

def test_empty_file(tmp_path):
    # Test with an entirely empty file
    test_input = tmp_path / "empty.txt"
    test_input.write_text("")
    
    empty_lines_count = remove_empty_lines(str(test_input))
    
    with open(test_input, 'r') as f:
        lines = f.readlines()
    
    assert empty_lines_count == 0
    assert lines == []

def test_file_not_found():
    # Test file not found error
    with pytest.raises(FileNotFoundError):
        remove_empty_lines("non_existent_file.txt")