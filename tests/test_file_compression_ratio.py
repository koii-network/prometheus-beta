import os
import pytest
import tempfile
import zlib

from src.file_compression_ratio import calculate_compression_ratio

def test_calculate_compression_ratio_typical():
    # Create a temporary file with compressible content
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        test_content = b'test ' * 1000  # repetitive content compresses well
        temp_file.write(test_content)
        temp_file.flush()
        
        try:
            ratio = calculate_compression_ratio(temp_file.name)
            assert ratio > 1.0, "Compression ratio should be greater than 1.0 for compressible content"
        finally:
            os.unlink(temp_file.name)

def test_calculate_compression_ratio_noncompressible():
    # Create a temporary file with random (non-compressible) content
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        test_content = os.urandom(1000)
        temp_file.write(test_content)
        temp_file.flush()
        
        try:
            ratio = calculate_compression_ratio(temp_file.name)
            assert ratio == 1.0, "Compression ratio should be 1.0 for non-compressible content"
        finally:
            os.unlink(temp_file.name)

def test_calculate_compression_ratio_empty_file():
    # Create an empty temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'')
        temp_file.flush()
        
        try:
            ratio = calculate_compression_ratio(temp_file.name)
            assert ratio is None, "Empty file should return None"
        finally:
            os.unlink(temp_file.name)

def test_calculate_compression_ratio_nonexistent_file():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        calculate_compression_ratio('/path/to/nonexistent/file.txt')

def test_calculate_compression_ratio_permission_error(mocker):
    # Simulate a permission error when reading the file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'test content')
        temp_file.flush()
        
        try:
            # Mock the file open to raise a PermissionError
            mocker.patch('builtins.open', side_effect=PermissionError("Permission denied"))
            
            with pytest.raises(PermissionError):
                calculate_compression_ratio(temp_file.name)
        finally:
            os.unlink(temp_file.name)