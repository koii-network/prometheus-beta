"""
Tests for the file_append module.

This test suite covers various scenarios for the append_text_to_file function.
"""

import os
import pytest
import tempfile

from src.file_append import append_text_to_file


def test_successful_append():
    """Test that text can be successfully appended to an existing file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Initial content\n")
        temp_file.close()
        
        try:
            append_text_to_file(temp_file.name, "Additional text\n")
            
            with open(temp_file.name, 'r') as f:
                content = f.read()
                assert content == "Initial content\n" + "Additional text\n"
        finally:
            os.unlink(temp_file.name)


def test_append_empty_string():
    """Test appending an empty string."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Initial content\n")
        temp_file.close()
        
        try:
            append_text_to_file(temp_file.name, "")
            
            with open(temp_file.name, 'r') as f:
                content = f.read()
                assert content == "Initial content\n"
        finally:
            os.unlink(temp_file.name)


def test_nonexistent_file():
    """Test that attempting to append to a nonexistent file raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        nonexistent_file = os.path.join(temp_dir, 'nonexistent.txt')
        
        with pytest.raises(FileNotFoundError):
            append_text_to_file(nonexistent_file, "Text")


def test_input_type_errors():
    """Test type checking for input parameters."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            # Test non-string file path
            with pytest.raises(TypeError):
                append_text_to_file(123, "Text")
            
            # Test non-string text
            with pytest.raises(TypeError):
                append_text_to_file(temp_file.name, 456)
        finally:
            os.unlink(temp_file.name)


def test_empty_file_path():
    """Test that an empty file path raises a ValueError."""
    with pytest.raises(ValueError):
        append_text_to_file("", "Text")
    
    with pytest.raises(ValueError):
        append_text_to_file("   ", "Text")


def test_directory_path():
    """Test that attempting to append to a directory raises an IsADirectoryError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(IsADirectoryError):
            append_text_to_file(temp_dir, "Text")