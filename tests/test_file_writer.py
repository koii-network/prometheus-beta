import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file():
    # Test writing a simple string
    test_path = 'test_output.txt'
    test_content = 'Hello, world!'
    
    write_string_to_file(test_path, test_content)
    
    # Verify the file was created and contains the correct content
    assert os.path.exists(test_path)
    with open(test_path, 'r') as file:
        assert file.read() == test_content
    
    # Clean up the test file
    os.remove(test_path)

def test_write_empty_string():
    # Test writing an empty string
    test_path = 'empty_test.txt'
    test_content = ''
    
    write_string_to_file(test_path, test_content)
    
    # Verify the file was created and is empty
    assert os.path.exists(test_path)
    with open(test_path, 'r') as file:
        assert file.read() == ''
    
    # Clean up the test file
    os.remove(test_path)

def test_invalid_file_path_type():
    # Test passing non-string file path
    with pytest.raises(TypeError):
        write_string_to_file(123, 'content')

def test_invalid_content_type():
    # Test passing non-string content
    with pytest.raises(TypeError):
        write_string_to_file('test.txt', 123)

def test_empty_file_path():
    # Test passing an empty file path
    with pytest.raises(ValueError):
        write_string_to_file('', 'content')
    with pytest.raises(ValueError):
        write_string_to_file('   ', 'content')