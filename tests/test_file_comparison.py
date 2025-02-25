import os
import pytest
import tempfile

from src.file_comparison import are_files_identical

def test_identical_files():
    """Test that identical files return True"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        try:
            temp1.write("Hello, world!")
            temp2.write("Hello, world!")
            temp1.close()
            temp2.close()
            
            assert are_files_identical(temp1.name, temp2.name) is True
        finally:
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_different_files():
    """Test that different files return False"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        try:
            temp1.write("Hello, world!")
            temp2.write("Different content")
            temp1.close()
            temp2.close()
            
            assert are_files_identical(temp1.name, temp2.name) is False
        finally:
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_different_sized_files():
    """Test files with different sizes return False"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        try:
            temp1.write("Short")
            temp2.write("Longer content")
            temp1.close()
            temp2.close()
            
            assert are_files_identical(temp1.name, temp2.name) is False
        finally:
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_file_not_found():
    """Test that FileNotFoundError is raised for non-existent files"""
    with pytest.raises(FileNotFoundError):
        are_files_identical("/path/to/nonexistent/file1", "/path/to/nonexistent/file2")

def test_invalid_path_type():
    """Test that TypeError is raised for non-string path inputs"""
    with pytest.raises(TypeError):
        are_files_identical(123, "valid_path")
    with pytest.raises(TypeError):
        are_files_identical("valid_path", None)

def test_directory_comparison():
    """Test that comparing directories returns False"""
    assert are_files_identical(os.path.dirname(__file__), os.path.dirname(__file__)) is False

def test_empty_identical_files():
    """Test that empty files are considered identical"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        try:
            temp1.close()
            temp2.close()
            
            assert are_files_identical(temp1.name, temp2.name) is True
        finally:
            os.unlink(temp1.name)
            os.unlink(temp2.name)