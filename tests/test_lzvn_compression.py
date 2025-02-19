import pytest
from src.lzvn_compression import lzvn_compress, lzvn_decompress

def test_lzvn_compression_basic():
    # Test basic compression and decompression
    original = b'hello world hello world'
    compressed = lzvn_compress(original)
    assert compressed != original
    assert len(compressed) < len(original)
    
    decompressed = lzvn_decompress(compressed)
    assert decompressed == original

def test_lzvn_empty_input():
    # Test empty input
    assert lzvn_compress(b'') == b''
    assert lzvn_decompress(b'') == b''

def test_lzvn_repeated_patterns():
    # Test input with repeated patterns
    original = b'ABCABCABCABC' * 10
    compressed = lzvn_compress(original)
    assert len(compressed) < len(original)
    
    decompressed = lzvn_decompress(compressed)
    assert decompressed == original

def test_lzvn_invalid_input_type():
    # Test invalid input types
    with pytest.raises(TypeError):
        lzvn_compress('not bytes')
    with pytest.raises(TypeError):
        lzvn_decompress('not bytes')

def test_lzvn_random_data():
    # Test with random data
    import random
    original = bytes(random.randint(0, 255) for _ in range(1000))
    compressed = lzvn_compress(original)
    
    decompressed = lzvn_decompress(compressed)
    assert decompressed == original