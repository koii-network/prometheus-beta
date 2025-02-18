import os
import pytest
import tempfile
from src.zstandard_compression import compress_file, decompress_file

def create_test_file(content):
    """Helper function to create a temporary test file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(content.encode())
        return temp_file.name

def test_compression_and_decompression():
    """Test complete compression and decompression cycle."""
    # Create test file
    original_content = "Hello, Zstandard compression test!"
    input_path = create_test_file(original_content)
    
    try:
        # Compress the file
        compressed_path = compress_file(input_path)
        assert os.path.exists(compressed_path)
        assert compressed_path.endswith('.zst')
        
        # Decompress the file
        decompressed_path = decompress_file(compressed_path)
        assert os.path.exists(decompressed_path)
        
        # Verify content
        with open(decompressed_path, 'rb') as f:
            decompressed_content = f.read().decode()
        
        assert decompressed_content == original_content
    
    finally:
        # Clean up temporary files
        for path in [input_path, compressed_path, decompressed_path]:
            if os.path.exists(path):
                os.unlink(path)

def test_compression_invalid_level():
    """Test compression with invalid compression level."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Test content")
        temp_file_path = temp_file.name
    
    try:
        with pytest.raises(ValueError, match="Compression level must be between 1 and 22"):
            compress_file(temp_file_path, compression_level=23)
    
    finally:
        os.unlink(temp_file_path)

def test_compression_nonexistent_file():
    """Test compression of a nonexistent file."""
    with pytest.raises(FileNotFoundError):
        compress_file("/path/to/nonexistent/file.txt")

def test_decompression_nonexistent_file():
    """Test decompression of a nonexistent file."""
    with pytest.raises(FileNotFoundError):
        decompress_file("/path/to/nonexistent/file.zst")

def test_decompression_invalid_extension():
    """Test decompression of a file without .zst extension."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Test content")
        temp_file_path = temp_file.name
    
    try:
        with pytest.raises(ValueError, match="Input file must have .zst extension"):
            decompress_file(temp_file_path)
    
    finally:
        os.unlink(temp_file_path)