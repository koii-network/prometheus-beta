import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file():
    # Test writing a simple string
    test_file = 'test_output.txt'
    test_content = 'Hello, World!'
    write_string_to_file(test_file, test_content)
    
    # Verify file was created and content is correct
    assert os.path.exists(test_file), "File was not created"
    with open(test_file, 'r') as file:
        assert file.read() == test_content, "File content does not match"
    
    # Clean up
    os.remove(test_file)

def test_write_empty_string():
    # Test writing an empty string
    test_file = 'empty_test.txt'
    write_string_to_file(test_file, '')
    
    # Verify file was created and is empty
    assert os.path.exists(test_file), "File was not created"
    with open(test_file, 'r') as file:
        assert file.read() == '', "File should be empty"
    
    # Clean up
    os.remove(test_file)

def test_invalid_file_path_type():
    # Test invalid file path type
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, 'content')

def test_invalid_content_type():
    # Test invalid content type
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file('test.txt', 123)

def test_overwrite_existing_file():
    # Test overwriting an existing file
    test_file = 'overwrite_test.txt'
    
    # First write
    write_string_to_file(test_file, 'Initial content')
    
    # Overwrite
    new_content = 'New content'
    write_string_to_file(test_file, new_content)
    
    # Verify new content
    with open(test_file, 'r') as file:
        assert file.read() == new_content, "File was not overwritten correctly"
    
    # Clean up
    os.remove(test_file)