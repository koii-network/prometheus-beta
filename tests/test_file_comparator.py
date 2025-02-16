import os
import pytest
import tempfile
import shutil

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
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_different_files():
    # Create two different temporary files
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        temp1.write("Content 1")
        temp2.write("Content 2")
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) == False
        finally:
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_non_existent_file():
    # Test with non-existent file
    with pytest.raises(FileNotFoundError):
        are_files_identical("non_existent_file1.txt", "non_existent_file2.txt")

def test_directory_input():
    # Test with directory input
    with pytest.raises(IsADirectoryError):
        are_files_identical(".", "/tmp")

def test_large_files():
    # Create two large files with identical content
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        large_content = "A" * 1_000_000  # 1 million characters
        temp1.write(large_content)
        temp2.write(large_content)
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) == True
        finally:
            os.unlink(temp1.name)
            os.unlink(temp2.name)