"""
Tests for the file_reader module.
"""
import os
import pytest
import tempfile

from src.file_reader import read_file_contents

def test_read_file_contents_success():
    """Test successful file reading."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, world!")
        temp_file.close()
    
    try:
        content = read_file_contents(temp_file.name)
        assert content == "Hello, world!"
    finally:
        os.unlink(temp_file.name)

def test_read_file_contents_non_existent_file():
    """Test reading a non-existent file."""
    with pytest.raises(FileNotFoundError):
        read_file_contents('non_existent_file.txt')

def test_read_file_contents_directory():
    """Test attempting to read a directory."""
    with pytest.raises(IsADirectoryError):
        read_file_contents('.')

def test_read_file_contents_empty_file():
    """Test reading an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
    
    try:
        content = read_file_contents(temp_file.name)
        assert content == ""
    finally:
        os.unlink(temp_file.name)

def test_read_file_contents_unicode():
    """Test reading a file with unicode content."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write("こんにちは、世界！")
        temp_file.close()
    
    try:
        content = read_file_contents(temp_file.name)
        assert content == "こんにちは、世界！"
    finally:
        os.unlink(temp_file.name)