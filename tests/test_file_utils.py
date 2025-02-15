import os
import pytest
from src.file_utils import write_string_to_file

def test_write_string_to_file():
    # Test writing a simple string
    test_file = 'test_output.txt'
    test_content = 'Hello, World!'
    write_string_to_file(test_file, test_content)
    
    # Verify the file was created and contains the correct content
    assert os.path.exists(test_file), "File was not created"
    
    with open(test_file, 'r') as file:
        written_content = file.read()
    
    assert written_content == test_content, "File content does not match input"
    
    # Clean up test file
    os.remove(test_file)

def test_write_empty_string():
    # Test writing an empty string
    test_file = 'empty_test.txt'
    write_string_to_file(test_file, '')
    
    with open(test_file, 'r') as file:
        written_content = file.read()
    
    assert written_content == '', "Empty string not written correctly"
    
    # Clean up test file
    os.remove(test_file)

def test_invalid_input_type():
    # Test that TypeError is raised for non-string input
    with pytest.raises(TypeError, match="Content must be a string"):
        write_string_to_file('test.txt', 42)
    
    with pytest.raises(TypeError, match="Content must be a string"):
        write_string_to_file('test.txt', ['list', 'of', 'strings'])

def test_invalid_file_path():
    # Test behavior with an invalid file path (this depends on the OS)
    # Note: The specific error might vary, so we're checking for a general IOError
    with pytest.raises(IOError):
        write_string_to_file('/nonexistent/directory/test.txt', 'Some content')