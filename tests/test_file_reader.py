"""
Tests for the file_reader module.
"""

import os
import pytest
import tempfile
from src.file_reader import read_file_contents

def test_read_existing_file():
    """Test reading contents of an existing file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, world!")
        temp_file.close()
        
        try:
            contents = read_file_contents(temp_file.name)
            assert contents == "Hello, world!"
        finally:
            os.unlink(temp_file.name)

def test_read_empty_file():
    """Test reading an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            contents = read_file_contents(temp_file.name)
            assert contents == ""
        finally:
            os.unlink(temp_file.name)

def test_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        read_file_contents("non_existent_file.txt")

def test_is_directory():
    """Test handling of directory path."""
    with pytest.raises(IsADirectoryError):
        read_file_contents(tempfile.gettempdir())

def test_unicode_file():
    """Test reading a file with Unicode content."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write("Héllo, wörld! 🌍")
        temp_file.close()
        
        try:
            contents = read_file_contents(temp_file.name)
            assert contents == "Héllo, wörld! 🌍"
        finally:
            os.unlink(temp_file.name)