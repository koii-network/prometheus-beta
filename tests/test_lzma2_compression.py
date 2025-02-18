import pytest
import lzma

# Import the functions to test
from src.lzma2_compression import lzma2_compress, lzma2_decompress

def test_lzma2_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, World! This is a test of LZMA2 compression."
    compressed_data = lzma2_compress(original_data)
    
    # Verify compression reduces size
    assert len(compressed_data) < len(original_data)
    
    # Verify decompression works
    decompressed_data = lzma2_decompress(compressed_data)
    assert decompressed_data == original_data

def test_lzma2_compression_string():
    """Test compression with string input"""
    original_data = "Python is awesome for compression algorithms!"
    compressed_data = lzma2_compress(original_data)
    
    # Verify compression reduces size
    assert len(compressed_data) < len(original_data.encode('utf-8'))
    
    # Verify decompression works
    decompressed_data = lzma2_decompress(compressed_data)
    assert decompressed_data == original_data.encode('utf-8')

def test_lzma2_large_data():
    """Test compression with larger data"""
    original_data = b"A" * 10000  # Large repetitive data
    compressed_data = lzma2_compress(original_data)
    
    # Large repetitive data should compress very well
    assert len(compressed_data) < len(original_data)
    
    # Verify decompression works
    decompressed_data = lzma2_decompress(compressed_data)
    assert decompressed_data == original_data

def test_lzma2_error_handling():
    """Test error handling for invalid inputs"""
    # Empty input
    with pytest.raises(ValueError):
        lzma2_compress(b"")
    with pytest.raises(ValueError):
        lzma2_decompress(b"")
    
    # Invalid input type
    with pytest.raises(TypeError):
        lzma2_compress(123)
    with pytest.raises(TypeError):
        lzma2_decompress(123)
    
    # Corrupted compressed data
    corrupted_data = b"This is not valid compressed data"
    with pytest.raises(lzma.LZMAError):
        lzma2_decompress(corrupted_data)

def test_symmetric_compression():
    """Ensure compression and decompression are symmetric"""
    test_cases = [
        b"Short test",
        "Unicode test: こんにちは",
        b"0" * 1000,
        b"\x00\x01\x02\x03" * 100
    ]
    
    for data in test_cases:
        compressed = lzma2_compress(data)
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        decompressed = lzma2_decompress(compressed)
        assert decompressed == data