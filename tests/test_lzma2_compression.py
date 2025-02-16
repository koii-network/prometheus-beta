import pytest
import lzma
from src.lzma2_compression import lzma2_compress, lzma2_decompress

def test_lzma2_compression_and_decompression():
    """Test basic compression and decompression."""
    original_data = b"Hello, this is a test string for LZMA2 compression!"
    compressed = lzma2_compress(original_data)
    
    # Verify compression reduces size
    assert len(compressed) < len(original_data)
    
    # Verify decompression returns original data
    decompressed = lzma2_decompress(compressed)
    assert decompressed == original_data

def test_lzma2_compression_with_string():
    """Test compression with string input."""
    original_data = "Hello, world! Testing LZMA2 compression."
    compressed = lzma2_compress(original_data)
    decompressed = lzma2_decompress(compressed)
    
    assert decompressed.decode('utf-8') == original_data

def test_lzma2_large_data_compression():
    """Test compression with larger data."""
    original_data = b"A" * 100000  # Large repetitive data
    compressed = lzma2_compress(original_data)
    
    # Verify significant compression for repetitive data
    assert len(compressed) < len(original_data) * 0.5
    
    decompressed = lzma2_decompress(compressed)
    assert decompressed == original_data

def test_lzma2_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        lzma2_compress(12345)
    
    with pytest.raises(TypeError):
        lzma2_decompress(12345)

def test_lzma2_invalid_compressed_data():
    """Test handling of invalid compressed data."""
    with pytest.raises(lzma.LZMAError):
        lzma2_decompress(b"Invalid compressed data")