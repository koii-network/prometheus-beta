import os
import pytest
import tempfile
from src.file_appender import append_text_to_file

def test_append_text_to_existing_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Initial content\n")
        temp_file_path = temp_file.name
    
    try:
        # Append text to the file
        append_text_to_file(temp_file_path, "Additional text")
        
        # Read the file contents to verify appending
        with open(temp_file_path, 'r') as file:
            content = file.read()
        
        assert content == "Initial content\nAdditional text"
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_append_text_to_file_multiple_times():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("First line\n")
        temp_file_path = temp_file.name
    
    try:
        # Append multiple times
        append_text_to_file(temp_file_path, "Second line\n")
        append_text_to_file(temp_file_path, "Third line\n")
        
        # Read the file contents to verify appending
        with open(temp_file_path, 'r') as file:
            content = file.read()
        
        assert content == "First line\nSecond line\nThird line\n"
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_append_empty_string():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Existing content")
        temp_file_path = temp_file.name
    
    try:
        # Append empty string
        append_text_to_file(temp_file_path, "")
        
        # Read the file contents to verify no change
        with open(temp_file_path, 'r') as file:
            content = file.read()
        
        assert content == "Existing content"
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_file_not_found():
    # Create a unique file path that does not exist
    non_existent_path = os.path.join(tempfile.gettempdir(), f"non_existent_{os.getpid()}.txt")
    
    # Ensure the file truly does not exist
    assert not os.path.exists(non_existent_path), "Temporary file should not exist"
    
    # Test that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        append_text_to_file(non_existent_path, "Some text")

def test_invalid_input_types():
    # Test type checking
    with pytest.raises(TypeError):
        append_text_to_file(123, "Some text")
    
    with pytest.raises(TypeError):
        append_text_to_file("file.txt", 456)