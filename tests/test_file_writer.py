import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file():
    # Test writing a simple string
    test_file = 'test_output.txt'
    test_content = 'Hello, world!'
    write_string_to_file(test_file, test_content)
    
    # Verify the file was created and contains the correct content
    assert os.path.exists(test_file), "File was not created"
    with open(test_file, 'r') as file:
        assert file.read() == test_content, "File content does not match"
    
    # Clean up the test file
    os.remove(test_file)

def test_write_empty_string():
    # Test writing an empty string
    test_file = 'empty_test.txt'
    write_string_to_file(test_file, '')
    
    # Verify the file was created and is empty
    assert os.path.exists(test_file), "File was not created"
    with open(test_file, 'r') as file:
        assert file.read() == '', "File should be empty"
    
    # Clean up the test file
    os.remove(test_file)

def test_write_to_nonexistent_directory():
    # Test writing to a file in a nonexistent directory
    with pytest.raises(IOError, match="No such file or directory"):
        write_string_to_file('nonexistent/dir/test.txt', 'some content')

def test_write_to_readonly_file():
    # Simulate a readonly file scenario (this may vary slightly by OS)
    import os
    test_file = 'readonly_test.txt'
    
    # Create a file and make it read-only
    with open(test_file, 'w') as f:
        f.write('initial content')
    os.chmod(test_file, 0o444)  # read-only
    
    # Try to write to the read-only file
    with pytest.raises(IOError):
        write_string_to_file(test_file, 'new content')
    
    # Clean up and restore permissions
    os.chmod(test_file, 0o666)
    os.remove(test_file)