import os
import pytest
import tempfile
from src.file_compression import calculate_compression_ratio

def test_calculate_compression_ratio_text_file():
    # Create a temporary file with compressible content
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("This is a test file with repeating content " * 100)
        temp_file_path = temp_file.name
    
    try:
        # Calculate compression ratio
        ratio = calculate_compression_ratio(temp_file_path)
        
        # Assert that compression ratio is greater than 1 (compressed)
        assert ratio > 1.0
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_calculate_compression_ratio_binary_file():
    # Create a temporary binary file
    with tempfile.NamedTemporaryFile(mode='wb', delete=False) as temp_file:
        temp_file.write(os.urandom(1024))  # Random binary data
        temp_file_path = temp_file.name
    
    try:
        # Calculate compression ratio
        ratio = calculate_compression_ratio(temp_file_path)
        
        # Compression of random data might be close to 1
        assert 0.5 <= ratio <= 2.0
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_calculate_compression_ratio_empty_file():
    # Create an empty temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        # Expect a ValueError for empty file
        with pytest.raises(ValueError, match="Cannot calculate compression ratio for an empty file"):
            calculate_compression_ratio(temp_file_path)
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_calculate_compression_ratio_nonexistent_file():
    # Expect a FileNotFoundError for non-existent file
    with pytest.raises(FileNotFoundError):
        calculate_compression_ratio('/path/to/nonexistent/file.txt')