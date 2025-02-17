import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file():
    # Test writing a simple string to a file
    test_file = 'test_output.txt'
    test_content = 'Hello, world!'
    
    write_string_to_file(test_file, test_content)
    
    # Verify the file was created and contains the correct content
    assert os.path.exists(test_file)
    with open(test_file, 'r') as file:
        assert file.read() == test_content
    
    # Clean up test file
    os.remove(test_file)

def test_write_empty_string():
    # Test writing an empty string
    test_file = 'empty_test.txt'
    test_content = ''
    
    write_string_to_file(test_file, test_content)
    
    # Verify the file was created and is empty
    assert os.path.exists(test_file)
    with open(test_file, 'r') as file:
        assert file.read() == ''
    
    # Clean up test file
    os.remove(test_file)

def test_invalid_file_path():
    # Test error handling for invalid file paths
    with pytest.raises(TypeError):
        write_string_to_file(None, 'content')
    
    with pytest.raises(ValueError):
        write_string_to_file('', 'content')

def test_invalid_content():
    # Test error handling for invalid content
    with pytest.raises(TypeError):
        write_string_to_file('test.txt', None)