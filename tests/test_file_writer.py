import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file_success(tmp_path):
    # Create a test file path using tmp_path
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, World!"
    
    # Call the function
    write_string_to_file(str(test_file), test_content)
    
    # Verify the file was created and contains the correct content
    assert os.path.exists(test_file)
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == test_content

def test_write_string_to_file_overwrite(tmp_path):
    # Test that writing to an existing file overwrites its content
    test_file = tmp_path / "test_file.txt"
    
    # Write initial content
    write_string_to_file(str(test_file), "First content")
    
    # Overwrite with new content
    new_content = "Updated content"
    write_string_to_file(str(test_file), new_content)
    
    # Verify the new content
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == new_content

def test_write_string_to_file_empty_string(tmp_path):
    # Test writing an empty string
    test_file = tmp_path / "test_file.txt"
    write_string_to_file(str(test_file), "")
    
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == ""

def test_write_string_to_file_invalid_file_path_type():
    # Test invalid file path type
    with pytest.raises(TypeError, match="file_path and content must be strings"):
        write_string_to_file(123, "content")

def test_write_string_to_file_invalid_content_type():
    # Test invalid content type
    with pytest.raises(TypeError, match="file_path and content must be strings"):
        write_string_to_file("test.txt", 456)

def test_write_string_to_file_empty_file_path():
    # Test empty file path
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("", "content")