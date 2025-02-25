import os
import pytest
import tempfile
from src.xz_compression import compress_xz, decompress_xz


def test_compress_decompress_bytes():
    """Test compression and decompression of byte data."""
    original_data = b"Hello, this is a test of XZ compression!"
    
    # Compress
    compressed = compress_xz(original_data)
    assert compressed is not None
    assert len(compressed) > 0
    assert compressed != original_data
    
    # Decompress
    decompressed = decompress_xz(compressed)
    assert decompressed == original_data


def test_compress_decompress_string():
    """Test compression and decompression of string data."""
    original_data = "Hello, this is a test of XZ compression!"
    
    # Compress
    compressed = compress_xz(original_data)
    assert compressed is not None
    assert len(compressed) > 0
    assert compressed != original_data.encode('utf-8')
    
    # Decompress
    decompressed = decompress_xz(compressed)
    assert decompressed == original_data.encode('utf-8')


def test_compress_to_file():
    """Test compressing data to a file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_out:
        try:
            original_data = b"Compress this data to a file"
            
            # Compress to file
            compressed_data = compress_xz(original_data, output_path=temp_out.name)
            
            # Verify file was created and has content
            assert os.path.exists(temp_out.name)
            assert os.path.getsize(temp_out.name) > 0
            
            # Decompress and verify
            with open(temp_out.name, 'rb') as f:
                decompressed = decompress_xz(f)
            assert decompressed == original_data
        finally:
            os.unlink(temp_out.name)


def test_decompress_from_file():
    """Test decompressing data from a file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_out:
        try:
            original_data = b"Decompress this data from a file"
            
            # First compress to file
            compress_xz(original_data, output_path=temp_out.name)
            
            # Decompress from file
            decompressed = decompress_xz(temp_out.name)
            assert decompressed == original_data
        finally:
            os.unlink(temp_out.name)


def test_compression_levels():
    """Test different compression levels."""
    data = b"Test compression levels for XZ algorithm"
    
    # Test valid compression levels
    for level in range(10):
        compressed = compress_xz(data, compression_level=level)
        assert compressed is not None
        
        # Verify decompression works
        decompressed = decompress_xz(compressed)
        assert decompressed == data


def test_invalid_compression_level():
    """Test invalid compression level raises ValueError."""
    with pytest.raises(ValueError):
        compress_xz(b"Test data", compression_level=-1)
    
    with pytest.raises(ValueError):
        compress_xz(b"Test data", compression_level=10)


def test_invalid_input_type():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        compress_xz(123)
    
    with pytest.raises(TypeError):
        decompress_xz(123)


def test_empty_input():
    """Test compression and decompression of empty data."""
    empty_data = b""
    
    # Compress
    compressed = compress_xz(empty_data)
    assert compressed is not None
    
    # Decompress
    decompressed = decompress_xz(compressed)
    assert decompressed == empty_data