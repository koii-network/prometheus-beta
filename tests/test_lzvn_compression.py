import pytest
from src.lzvn_compression import lzvn_compress, lzvn_decompress

def test_lzvn_compression_and_decompression():
    # Test simple string compression and decompression
    original_data = b"hello world hello world hello world"
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    assert decompressed == original_data

def test_repeated_patterns():
    # Test data with repeated patterns
    repeated_data = b"abcabcabcabcabcabc" * 10
    compressed = lzvn_compress(repeated_data)
    decompressed = lzvn_decompress(compressed)
    assert decompressed == repeated_data

def test_empty_input():
    # Test empty input for both compress and decompress
    assert lzvn_compress(b'') == b''
    assert lzvn_decompress(b'') == b''

def test_random_data():
    # Test with some random data
    import random
    random.seed(42)
    random_data = bytes(random.randint(0, 255) for _ in range(1000))
    compressed = lzvn_compress(random_data)
    decompressed = lzvn_decompress(compressed)
    assert decompressed == random_data

def test_input_type_validation():
    # Test type validation
    with pytest.raises(TypeError):
        lzvn_compress("not bytes")
    with pytest.raises(TypeError):
        lzvn_decompress("not bytes")

def test_compression_ratio():
    # Test that compression reduces data size or at least doesn't significantly increase it
    test_data = b"hello world " * 100
    compressed = lzvn_compress(test_data)
    assert len(compressed) <= len(test_data)

def test_large_data():
    # Test with a larger piece of data
    large_data = b"This is a test of large data compression. " * 1000
    compressed = lzvn_compress(large_data)
    decompressed = lzvn_decompress(compressed)
    assert decompressed == large_data