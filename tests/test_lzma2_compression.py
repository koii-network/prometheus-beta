import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzma2_compression import compress_lzma2, decompress_lzma2

def test_compress_decompress_string():
    """Test compression and decompression of a simple string."""
    original_text = "Hello, world! This is a test of LZMA2 compression."
    compressed = compress_lzma2(original_text)
    assert compressed is not None
    assert len(compressed) < len(original_text.encode('utf-8'))
    
    decompressed = decompress_lzma2(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes."""
    original_bytes = b'\x00\x01\x02\x03\x04' * 100
    compressed = compress_lzma2(original_bytes)
    assert compressed is not None
    assert len(compressed) < len(original_bytes)
    
    decompressed = decompress_lzma2(compressed)
    assert decompressed == original_bytes

def test_different_compression_presets():
    """Test different compression presets."""
    text = "Test compression with different presets" * 100
    
    # Test various presets
    for preset in [0, 3, 6, 9]:
        compressed = compress_lzma2(text, preset=preset)
        assert compressed is not None
        
        decompressed = decompress_lzma2(compressed)
        assert decompressed.decode('utf-8') == text

def test_edge_cases():
    """Test edge cases and error handling."""
    # Empty string
    empty_str = ""
    compressed_empty = compress_lzma2(empty_str)
    assert decompress_lzma2(compressed_empty) == b''

    # Very large input
    large_text = "A" * (1024 * 1024)  # 1MB of text
    compressed_large = compress_lzma2(large_text)
    assert decompress_lzma2(compressed_large).decode('utf-8') == large_text

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Invalid compression preset
    with pytest.raises(ValueError):
        compress_lzma2("test", preset=10)
    
    # Invalid input type
    with pytest.raises(TypeError):
        compress_lzma2(123)
    
    # Invalid compressed data for decompression
    with pytest.raises(RuntimeError):
        decompress_lzma2(b'invalid_data')
    
    # Empty input for decompression
    with pytest.raises(ValueError):
        decompress_lzma2(b'')