import os
import pytest
import tempfile
from src.file_comparison import are_files_identical

def test_identical_files():
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
    # Create two different temporary files
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        temp1.write("File 1 content")
        temp2.write("File 2 content")
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) is False
        finally:
            # Clean up temporary files
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_nonexistent_file():
    # Test when a file does not exist
    with pytest.raises(FileNotFoundError):
        are_files_identical("nonexistent_file1.txt", "nonexistent_file2.txt")

def test_different_sized_files():
    # Create two files with different sizes
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        temp1.write("Short content")
        temp2.write("Longer content that is different")
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) is False
        finally:
            # Clean up temporary files
            os.unlink(temp1.name)
            os.unlink(temp2.name)