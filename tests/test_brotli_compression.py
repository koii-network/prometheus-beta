import pytest
import src.brotli_compression as brotli_comp

def test_compress_decompress_string():
    """Test compression and decompression of a string."""
    original = "Hello, World! This is a test of Brotli compression."
    compressed = brotli_comp.compress_brotli(original)
    assert compressed != original.encode('utf-8')
    
    decompressed = brotli_comp.decompress_brotli(compressed)
    assert decompressed.decode('utf-8') == original

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes."""
    original = b"Binary data compression test!"
    compressed = brotli_comp.compress_brotli(original)
    assert compressed != original
    
    decompressed = brotli_comp.decompress_brotli(compressed)
    assert decompressed == original

def test_compression_quality():
    """Test different compression qualities."""
    data = "Compression quality test" * 100
    
    # Test default (max) quality
    compressed_max = brotli_comp.compress_brotli(data)
    
    # Test low quality
    compressed_low = brotli_comp.compress_brotli(data, quality=0)
    
    assert len(compressed_max) < len(compressed_low)

def test_invalid_compression_quality():
    """Test invalid compression quality raises ValueError."""
    with pytest.raises(ValueError):
        brotli_comp.compress_brotli("test", quality=12)
    
    with pytest.raises(ValueError):
        brotli_comp.compress_brotli("test", quality=-1)

def test_invalid_input_types():
    """Test invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        brotli_comp.compress_brotli(123)
    
    with pytest.raises(TypeError):
        brotli_comp.decompress_brotli("not bytes")

def test_empty_input():
    """Test compression and decompression of empty input."""
    empty_str = ""
    empty_bytes = b""
    
    # String compression
    compressed_str = brotli_comp.compress_brotli(empty_str)
    assert brotli_comp.decompress_brotli(compressed_str) == empty_str.encode('utf-8')
    
    # Bytes compression
    compressed_bytes = brotli_comp.compress_brotli(empty_bytes)
    assert brotli_comp.decompress_brotli(compressed_bytes) == empty_bytes