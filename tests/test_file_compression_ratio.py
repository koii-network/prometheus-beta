import os
import pytest
import tempfile
from src.file_compression_ratio import calculate_compression_ratio

def test_calculate_compression_ratio_text_file():
    # Create a temporary text file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, this is a test file for compression ratio")
        temp_file_path = temp_file.name
    
    try:
        ratio = calculate_compression_ratio(temp_file_path)
        assert 0 < ratio < 1, f"Compression ratio {ratio} should be between 0 and 1"
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_calculate_compression_ratio_binary_file():
    # Create a temporary binary file
    with tempfile.NamedTemporaryFile(mode='wb', delete=False) as temp_file:
        temp_file.write(b'\x00' * 1000)  # Write 1000 zero bytes
        temp_file_path = temp_file.name
    
    try:
        ratio = calculate_compression_ratio(temp_file_path)
        assert 0 < ratio < 1, f"Compression ratio {ratio} should be between 0 and 1"
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_calculate_compression_ratio_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        calculate_compression_ratio('nonexistent_file.txt')

def test_calculate_compression_ratio_empty_file():
    # Create an empty temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        with pytest.raises(ValueError, match="Cannot calculate compression ratio for an empty file"):
            calculate_compression_ratio(temp_file_path)
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)