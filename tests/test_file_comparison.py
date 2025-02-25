import os
import pytest
import tempfile
import shutil

from src.file_comparison import are_files_identical

def test_identical_files():
    """Test that identical files are recognized as identical."""
    # Create two identical temporary files
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        content = "This is a test file content"
        temp1.write(content)
        temp2.write(content)
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) is True
        finally:
            # Clean up temporary files
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_different_files():
    """Test that different files are recognized as different."""
    # Create two different temporary files
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        temp1.write("First content")
        temp2.write("Second content")
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) is False
        finally:
            # Clean up temporary files
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_empty_files():
    """Test that two empty files are identical."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) is True
        finally:
            # Clean up temporary files
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_nonexistent_file():
    """Test that a FileNotFoundError is raised for nonexistent files."""
    with pytest.raises(FileNotFoundError):
        are_files_identical("/path/to/nonexistent/file1", "/path/to/nonexistent/file2")

def test_files_with_different_size():
    """Test files with different sizes."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        temp1.write("Short content")
        temp2.write("Much longer content that is different")
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) is False
        finally:
            # Clean up temporary files
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_large_files():
    """Test comparison of large files."""
    # Create a large file
    with tempfile.NamedTemporaryFile(mode='wb', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='wb', delete=False) as temp2:
        # Generate 1MB of random data
        large_content = os.urandom(1024 * 1024)
        temp1.write(large_content)
        temp2.write(large_content)
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) is True
        finally:
            # Clean up temporary files
            os.unlink(temp1.name)
            os.unlink(temp2.name)