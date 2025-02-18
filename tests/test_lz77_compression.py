import pytest
from src.lz77_compression import LZ77

def test_lz77_compression_basic():
    """Test basic compression and decompression"""
    original = "ABCABCABCABC"
    compressed = LZ77.compress(original)
    decompressed = LZ77.decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_compression_repeated_pattern():
    """Test compression with repeated patterns"""
    original = "Hello, hello, hello! Hello, hello!"
    compressed = LZ77.compress(original)
    decompressed = LZ77.decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_compression_empty_string():
    """Test compression and decompression of an empty string"""
    original = ""
    compressed = LZ77.compress(original)
    decompressed = LZ77.decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_compression_bytes():
    """Test compression and decompression of byte data"""
    original = b'\x00\x01\x02\x00\x01\x02\x00\x01\x02'
    compressed = LZ77.compress(original)
    decompressed = LZ77.decompress(compressed)
    assert decompressed == original

def test_lz77_compression_long_text():
    """Test compression of a longer text"""
    original = "The quick brown fox jumps over the lazy dog " * 10
    compressed = LZ77.compress(original)
    decompressed = LZ77.decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_compression_custom_window_size():
    """Test compression with custom window and lookahead buffer sizes"""
    original = "ABCABCABCABC" * 5
    compressed = LZ77.compress(original, window_size=512, lookahead_buffer_size=32)
    decompressed = LZ77.decompress(compressed)
    assert decompressed.decode('utf-8') == original