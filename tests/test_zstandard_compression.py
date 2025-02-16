import os
import pytest
import tempfile
from src.zstandard_compression import compress_file, decompress_file

def create_test_file(content='Test content for compression'):
    """Helper function to create a temporary test file."""
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write(content)
        return temp_file.name

def test_compress_file():
    # Create a temporary test file
    input_file = create_test_file()
    try:
        # Compress the file
        compressed_file = compress_file(input_file)
        
        # Check compressed file exists and has .zst extension
        assert os.path.exists(compressed_file)
        assert compressed_file.endswith('.zst')
        
        # Check compressed file size is smaller than original
        original_size = os.path.getsize(input_file)
        compressed_size = os.path.getsize(compressed_file)
        assert compressed_size < original_size
    finally:
        # Clean up files
        os.unlink(input_file)
        os.unlink(compressed_file)

def test_decompress_file():
    # Create a temporary test file
    original_content = 'Test content for decompression'
    input_file = create_test_file(original_content)
    try:
        # Compress the file
        compressed_file = compress_file(input_file)
        
        # Decompress the file
        decompressed_file = decompress_file(compressed_file)
        
        # Check decompressed file exists
        assert os.path.exists(decompressed_file)
        
        # Verify decompressed content
        with open(decompressed_file, 'r') as f:
            assert f.read() == original_content
    finally:
        # Clean up files
        os.unlink(input_file)
        os.unlink(compressed_file)
        os.unlink(decompressed_file)

def test_invalid_compression_level():
    input_file = create_test_file()
    try:
        # Test invalid compression level
        with pytest.raises(ValueError):
            compress_file(input_file, compression_level=0)
        with pytest.raises(ValueError):
            compress_file(input_file, compression_level=23)
    finally:
        os.unlink(input_file)

def test_nonexistent_input_file():
    # Test with nonexistent input file
    with pytest.raises(FileNotFoundError):
        compress_file('/path/to/nonexistent/file')
    
    with pytest.raises(FileNotFoundError):
        decompress_file('/path/to/nonexistent/file.zst')

def test_invalid_decompress_input():
    # Create a temporary file without .zst extension
    input_file = create_test_file()
    try:
        with pytest.raises(ValueError):
            decompress_file(input_file)
    finally:
        os.unlink(input_file)