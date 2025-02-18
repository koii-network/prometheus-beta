import os
import pytest
import tempfile
from src.file_comparator import are_files_identical

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
            assert are_files_identical(temp1.name, temp2.name) == True
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
            assert are_files_identical(temp1.name, temp2.name) == False
        finally:
            # Clean up temporary files
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        are_files_identical("nonexistent_file1.txt", "nonexistent_file2.txt")

def test_empty_files():
    # Create two empty temporary files
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) == True
        finally:
            # Clean up temporary files
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_large_files():
    # Create two large files with identical content
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        large_content = "A" * (1024 * 1024)  # 1MB of content
        temp1.write(large_content)
        temp2.write(large_content)
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) == True
        finally:
            # Clean up temporary files
            os.unlink(temp1.name)
            os.unlink(temp2.name)