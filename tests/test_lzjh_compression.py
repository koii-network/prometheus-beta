import pytest
from src.lzjh_compression import lzjh_compress, lzjh_decompress

def test_basic_compression_decompression():
    # Test basic string compression and decompression
    original = "Hello, world!"
    compressed = lzjh_compress(original.encode('utf-8'))
    decompressed = lzjh_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_repeated_patterns():
    # Test compression of repeated patterns
    original = "ABABABABABABAB"
    compressed = lzjh_compress(original.encode('utf-8'))
    decompressed = lzjh_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_empty_input():
    # Test compression and decompression of empty input
    original = ""
    compressed = lzjh_compress(original.encode('utf-8'))
    decompressed = lzjh_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_unicode_input():
    # Test compression of unicode characters
    original = "こんにちは、世界！"
    compressed = lzjh_compress(original.encode('utf-8'))
    decompressed = lzjh_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_binary_data():
    # Test compression of binary data
    original = bytes([0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5])
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original

def test_random_data():
    # Test compression of random bytes
    import random
    random.seed(42)  # For reproducibility
    original = bytes(random.getrandbits(8) for _ in range(1000))
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original