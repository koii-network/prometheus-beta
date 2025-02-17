import os
import pytest
import tempfile
from src.file_comparison import are_files_identical

def test_identical_files():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as f2:
        content = "This is a test file content"
        f1.write(content)
        f2.write(content)
        f1.close()
        f2.close()
        
        try:
            assert are_files_identical(f1.name, f2.name) == True
        finally:
            os.unlink(f1.name)
            os.unlink(f2.name)

def test_different_files():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as f2:
        f1.write("File 1 content")
        f2.write("File 2 content")
        f1.close()
        f2.close()
        
        try:
            assert are_files_identical(f1.name, f2.name) == False
        finally:
            os.unlink(f1.name)
            os.unlink(f2.name)

def test_non_existent_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write("Test content")
        f.close()
        
        try:
            with pytest.raises(FileNotFoundError):
                are_files_identical(f.name, "/path/to/non/existent/file")
        finally:
            os.unlink(f.name)

def test_empty_files():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as f2:
        f1.close()
        f2.close()
        
        try:
            assert are_files_identical(f1.name, f2.name) == True
        finally:
            os.unlink(f1.name)
            os.unlink(f2.name)

def test_large_files():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as f2:
        large_content = "A" * 1_000_000
        f1.write(large_content)
        f2.write(large_content)
        f1.close()
        f2.close()
        
        try:
            assert are_files_identical(f1.name, f2.name) == True
        finally:
            os.unlink(f1.name)
            os.unlink(f2.name)