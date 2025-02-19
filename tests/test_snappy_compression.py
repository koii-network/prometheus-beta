import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from snappy_compression import snappy_compress, snappy_decompress

def test_snappy_compression_with_string():
    """Test compression and decompression with a string input."""
    original_data = "Hello, Snappy compression!"
    compressed = snappy_compress(original_data)
    decompressed = snappy_decompress(compressed)
    
    assert decompressed.decode('utf-8') == original_data
    assert len(compressed) < len(original_data.encode('utf-8'))

def test_snappy_compression_with_bytes():
    """Test compression and decompression with bytes input."""
    original_data = b"Binary data for Snappy compression test"
    compressed = snappy_compress(original_data)
    decompressed = snappy_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)

def test_snappy_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        snappy_compress("")
    
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        snappy_decompress(b"")

def test_snappy_invalid_input_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        snappy_compress(123)
    
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        snappy_decompress("not bytes")

def test_snappy_round_trip_large_data():
    """Test compression and decompression with a larger dataset."""
    original_data = "A" * 10000  # Large repetitive string
    compressed = snappy_compress(original_data)
    decompressed = snappy_decompress(compressed)
    
    assert decompressed.decode('utf-8') == original_data
    assert len(compressed) < len(original_data)

def test_different_compression_levels():
    """Verify that different inputs compress differently."""
    data1 = "Repeated text " * 100
    data2 = "Random unique text that won't compress well"
    
    compressed1 = snappy_compress(data1)
    compressed2 = snappy_compress(data2)
    
    assert len(compressed1) < len(data1)
    assert len(compressed2) >= 0  # Might not compress much
    assert compressed1 != compressed2