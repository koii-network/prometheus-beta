import os
import pytest
import tempfile
from src.file_reader import read_text_file

def test_read_existing_text_file():
    # Create a temporary file with known content
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, World!")
        temp_file_path = temp_file.name

    try:
        # Read the file and verify content
        content = read_text_file(temp_file_path)
        assert content == "Hello, World!"
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_read_file_with_multiple_lines():
    # Create a temporary file with multiple lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Line 1\nLine 2\nLine 3")
        temp_file_path = temp_file.name

    try:
        # Read the file and verify content
        content = read_text_file(temp_file_path)
        assert content == "Line 1\nLine 2\nLine 3"
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_read_nonexistent_file():
    # Test reading a file that does not exist
    with pytest.raises(FileNotFoundError):
        read_text_file("nonexistent_file.txt")

def test_read_empty_file():
    # Create a temporary empty file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file_path = temp_file.name

    try:
        # Read the empty file
        content = read_text_file(temp_file_path)
        assert content == ""
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)