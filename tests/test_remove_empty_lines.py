import os
import pytest
import tempfile

from src.remove_empty_lines import remove_empty_lines

def test_remove_empty_lines_inplace():
    # Create a temporary file with empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello\n\n\nWorld\n   \nPython\n")
        temp_filename = temp_file.name

    try:
        # Remove empty lines in-place
        remove_empty_lines(temp_filename)

        # Check file contents
        with open(temp_filename, 'r') as f:
            lines = f.readlines()
        
        assert lines == ["Hello\n", "World\n", "Python\n"]
    finally:
        # Clean up temporary file
        os.unlink(temp_filename)

def test_remove_empty_lines_to_new_file():
    # Create a temporary input file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as input_file:
        input_file.write("Hello\n\n\nWorld\n   \nPython\n")
        input_filename = input_file.name

    # Create a temporary output file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as output_file:
        output_filename = output_file.name

    try:
        # Remove empty lines to new file
        remove_empty_lines(input_filename, output_filename)

        # Check output file contents
        with open(output_filename, 'r') as f:
            lines = f.readlines()
        
        assert lines == ["Hello\n", "World\n", "Python\n"]

        # Ensure input file is unchanged
        with open(input_filename, 'r') as f:
            original_lines = f.readlines()
        
        assert original_lines == ["Hello\n", "\n", "\n", "World\n", "   \n", "Python\n"]
    finally:
        # Clean up temporary files
        os.unlink(input_filename)
        os.unlink(output_filename)

def test_remove_empty_lines_all_empty():
    # Create a temporary file with only empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("\n\n   \n\t\n")
        temp_filename = temp_file.name

    try:
        # Remove empty lines
        remove_empty_lines(temp_filename)

        # Check file contents
        with open(temp_filename, 'r') as f:
            lines = f.readlines()
        
        assert lines == []
    finally:
        # Clean up temporary file
        os.unlink(temp_filename)

def test_remove_empty_lines_no_empty():
    # Create a temporary file with no empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello\nWorld\nPython\n")
        temp_filename = temp_file.name

    try:
        # Remove empty lines
        remove_empty_lines(temp_filename)

        # Check file contents
        with open(temp_filename, 'r') as f:
            lines = f.readlines()
        
        assert lines == ["Hello\n", "World\n", "Python\n"]
    finally:
        # Clean up temporary file
        os.unlink(temp_filename)

def test_remove_empty_lines_nonexistent_file():
    # Test with a non-existent file
    with pytest.raises(FileNotFoundError):
        remove_empty_lines("/path/to/nonexistent/file.txt")

def test_remove_empty_lines_empty_file():
    # Create an empty temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_filename = temp_file.name

    try:
        # Remove empty lines from empty file
        remove_empty_lines(temp_filename)

        # Check file contents
        with open(temp_filename, 'r') as f:
            lines = f.readlines()
        
        assert lines == []
    finally:
        # Clean up temporary file
        os.unlink(temp_filename)