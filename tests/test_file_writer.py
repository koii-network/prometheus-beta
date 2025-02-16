import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file():
    # Test writing a simple string
    test_file = 'test_output.txt'
    test_content = 'Hello, World!'
    write_string_to_file(test_file, test_content)
    
    # Verify the file was created and contains the correct content
    assert os.path.exists(test_file)
    with open(test_file, 'r') as file:
        assert file.read() == test_content
    
    # Clean up the test file
    os.remove(test_file)

def test_write_empty_string():
    # Test writing an empty string
    test_file = 'empty_test.txt'
    write_string_to_file(test_file, '')
    
    # Verify the file was created and is empty
    assert os.path.exists(test_file)
    with open(test_file, 'r') as file:
        assert file.read() == ''
    
    # Clean up the test file
    os.remove(test_file)

def test_invalid_file_path_type():
    # Test invalid file path type
    with pytest.raises(TypeError):
        write_string_to_file(123, 'content')

def test_invalid_content_type():
    # Test invalid content type
    with pytest.raises(TypeError):
        write_string_to_file('test.txt', 123)

def test_empty_file_path():
    # Test empty file path
    with pytest.raises(ValueError):
        write_string_to_file('', 'content')