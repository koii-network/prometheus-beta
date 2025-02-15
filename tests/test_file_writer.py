import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file():
    # Test basic functionality
    test_file = 'test_output.txt'
    test_content = 'Hello, world!'
    
    write_string_to_file(test_file, test_content)
    
    # Verify file was created and content is correct
    assert os.path.exists(test_file)
    with open(test_file, 'r') as file:
        assert file.read() == test_content
    
    # Clean up test file
    os.remove(test_file)

def test_write_empty_string():
    # Test writing an empty string
    test_file = 'empty_file.txt'
    
    write_string_to_file(test_file, '')
    
    # Verify file was created and is empty
    assert os.path.exists(test_file)
    with open(test_file, 'r') as file:
        assert file.read() == ''
    
    # Clean up test file
    os.remove(test_file)

def test_invalid_file_path_type():
    # Test invalid file path type
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, 'content')

def test_invalid_content_type():
    # Test invalid content type
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file('test.txt', 123)

def test_empty_file_path():
    # Test empty file path
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file('', 'content')