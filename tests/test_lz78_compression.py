import pytest
from src.lz78_compression import LZ78Compressor

def test_lz78_empty_string():
    """Test compression and decompression of an empty string."""
    text = ''
    compressed = LZ78Compressor.compress(text)
    assert compressed == []
    
    decompressed = LZ78Compressor.decompress(compressed)
    assert decompressed == text

def test_lz78_simple_repetitive_string():
    """Test compression of a simple repetitive string."""
    text = 'aaaaaaaa'
    compressed = LZ78Compressor.compress(text)
    decompressed = LZ78Compressor.decompress(compressed)
    assert decompressed == text

def test_lz78_mixed_string():
    """Test compression of a mixed string with repeated patterns."""
    text = 'banana banana'
    compressed = LZ78Compressor.compress(text)
    decompressed = LZ78Compressor.decompress(compressed)
    assert decompressed == text

def test_lz78_complex_string():
    """Test compression of a more complex string with various patterns."""
    text = 'the quick brown fox jumps over the lazy dog'
    compressed = LZ78Compressor.compress(text)
    decompressed = LZ78Compressor.decompress(compressed)
    assert decompressed == text

def test_lz78_unicode_string():
    """Test compression with unicode characters."""
    text = '👍 Hello, 世界! 👋'
    compressed = LZ78Compressor.compress(text)
    decompressed = LZ78Compressor.decompress(compressed)
    assert decompressed == text

def test_lz78_large_data():
    """Test compression of a large repetitive string."""
    text = 'abcdefg' * 1000
    compressed = LZ78Compressor.compress(text)
    decompressed = LZ78Compressor.decompress(compressed)
    assert decompressed == text

def test_lz78_compression_efficiency():
    """Verify that compression reduces string length for repetitive data."""
    text = 'repeat ' * 100
    compressed = LZ78Compressor.compress(text)
    assert len(compressed) < len(text)  # Compressed data should be smaller