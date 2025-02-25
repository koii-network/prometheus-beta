import os
import pytest
import tempfile

from src.zstandard_compress import (
    compress_data, 
    decompress_data, 
    compress_file, 
    decompress_file
)


def test_compress_decompress_bytes():
    """Test compressing and decompressing bytes"""
    original_data = b"Hello, Zstandard compression!"
    compressed = compress_data(original_data)
    
    # Verify compressed data is different
    assert compressed != original_data
    assert len(compressed) < len(original_data)
    
    # Decompress and verify
    decompressed = decompress_data(compressed)
    assert decompressed == original_data


def test_compress_decompress_string():
    """Test compressing and decompressing string"""
    original_data = "Hello, Zstandard compression!"
    compressed = compress_data(original_data)
    
    # Verify compressed data is different
    assert compressed != original_data.encode('utf-8')
    
    # Decompress and verify
    decompressed = decompress_data(compressed)
    assert decompressed == original_data.encode('utf-8')


def test_compression_levels():
    """Test different compression levels"""
    data = b"Test compression with different levels"
    
    # Test minimum and maximum levels
    min_compressed = compress_data(data, compression_level=1)
    max_compressed = compress_data(data, compression_level=22)
    
    # Verify different levels produce different compressed sizes
    assert len(min_compressed) != len(max_compressed)
    
    # Verify both can be decompressed
    assert decompress_data(min_compressed) == data
    assert decompress_data(max_compressed) == data


def test_file_compression():
    """Test file compression and decompression"""
    # Create a temporary file with test data
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        temp_input.write(b"Test file compression with Zstandard")
        input_path = temp_input.name

    try:
        # Compress the file
        compressed_path = compress_file(input_path)
        assert os.path.exists(compressed_path)
        
        # Decompress the file
        decompressed_path = decompress_file(compressed_path)
        assert os.path.exists(decompressed_path)
        
        # Verify file contents
        with open(decompressed_path, 'rb') as f:
            decompressed_content = f.read()
        
        assert decompressed_content == b"Test file compression with Zstandard"
    
    finally:
        # Clean up temp files
        for path in [input_path, compressed_path, decompressed_path]:
            if os.path.exists(path):
                os.unlink(path)


def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test invalid types
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data(123)
    
    # Test invalid compression level
    with pytest.raises(ValueError):
        compress_data(b"test", compression_level=0)
    
    with pytest.raises(ValueError):
        compress_data(b"test", compression_level=23)
    
    # Test non-existent files
    with pytest.raises(FileNotFoundError):
        compress_file("/path/to/nonexistent/file")
    
    with pytest.raises(FileNotFoundError):
        decompress_file("/path/to/nonexistent/file")


def test_large_data_compression():
    """Test compression of larger data"""
    large_data = b"0" * (1024 * 1024)  # 1MB of zeros
    compressed = compress_data(large_data)
    
    # Verify compression reduces size
    assert len(compressed) < len(large_data)
    
    # Verify decompression
    decompressed = decompress_data(compressed)
    assert decompressed == large_data