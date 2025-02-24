import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file_success():
    """Test writing a string to a file successfully."""
    test_file = 'test_output.txt'
    test_content = 'Hello, World!'
    
    write_string_to_file(test_file, test_content)
    
    # Verify file was created and contains correct content
    assert os.path.exists(test_file)
    with open(test_file, 'r') as file:
        assert file.read() == test_content
    
    # Clean up test file
    os.remove(test_file)

def test_write_string_to_file_overwrite():
    """Test that writing to an existing file overwrites its content."""
    test_file = 'test_overwrite.txt'
    
    # Write initial content
    write_string_to_file(test_file, 'Initial content')
    
    # Overwrite with new content
    new_content = 'Overwritten content'
    write_string_to_file(test_file, new_content)
    
    # Verify new content
    with open(test_file, 'r') as file:
        assert file.read() == new_content
    
    # Clean up test file
    os.remove(test_file)

def test_write_string_to_file_empty_string():
    """Test writing an empty string to a file."""
    test_file = 'test_empty.txt'
    
    write_string_to_file(test_file, '')
    
    # Verify file was created and is empty
    assert os.path.exists(test_file)
    with open(test_file, 'r') as file:
        assert file.read() == ''
    
    # Clean up test file
    os.remove(test_file)

def test_write_string_to_file_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Both file_path and content must be strings"):
        write_string_to_file(123, 'content')
    
    with pytest.raises(TypeError, match="Both file_path and content must be strings"):
        write_string_to_file('file.txt', 456)

def test_write_string_to_file_empty_path():
    """Test error handling for empty file path."""
    with pytest.raises(ValueError, match="File path cannot be an empty string"):
        write_string_to_file('', 'content')