import pytest
from src.lzrw_compression import lzrw_compress, lzrw_decompress

def test_compression_decompression_basic():
    """Test basic compression and decompression."""
    original_data = b"Hello, world! This is a test of LZRW compression."
    compressed = lzrw_compress(original_data)
    decompressed = lzrw_decompress(compressed)
    assert decompressed == original_data

def test_empty_input():
    """Test compression and decompression of empty input."""
    assert lzrw_compress(b'') == b''
    assert lzrw_decompress(b'') == b''

def test_repeated_data():
    """Test compression of data with repeated patterns."""
    repeated_data = b"AAAAAAAAAAAAAAAA"
    compressed = lzrw_compress(repeated_data)
    decompressed = lzrw_decompress(compressed)
    assert decompressed == repeated_data

def test_invalid_input_type():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        lzrw_compress("Not bytes")
    with pytest.raises(TypeError):
        lzrw_decompress("Not bytes")

def test_random_data():
    """Test compression and decompression of random data."""
    import random
    random.seed(42)  # For reproducibility
    random_data = bytes(random.randint(0, 255) for _ in range(1000))
    compressed = lzrw_compress(random_data)
    decompressed = lzrw_decompress(compressed)
    assert decompressed == random_data

def test_compression_ratio():
    """Verify that compression works on compressible data."""
    compressible_data = b"Hello " * 100
    compressed = lzrw_compress(compressible_data)
    assert len(compressed) < len(compressible_data)
    assert lzrw_decompress(compressed) == compressible_data