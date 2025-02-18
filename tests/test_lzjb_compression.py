import pytest
from src.lzjb_compression import lzjb_compress, lzjb_decompress

def test_lzjb_compression_decompression():
    # Test various input types and lengths
    test_cases = [
        b'Hello, World!',
        b'',
        b'aaaaaaaaaaaaaaaaaaaa',  # Repetitive data
        b'\x00\x01\x02\x03\x04\x05',  # Consecutive bytes
        b'This is a test of the LZJB compression algorithm',
        bytes(range(256)) * 10  # Large, varied input
    ]
    
    for original_data in test_cases:
        # Compress
        compressed = lzjb_compress(original_data)
        
        # Decompress
        decompressed = lzjb_decompress(compressed)
        
        # Verify
        assert decompressed == original_data, f"Failed for input: {original_data}"
        assert len(compressed) <= len(original_data), "Compressed data must not be larger than original"

def test_lzjb_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError):
        lzjb_compress("not bytes")
    
    with pytest.raises(TypeError):
        lzjb_decompress("not bytes")

def test_lzjb_edge_cases():
    # Empty input
    assert lzjb_compress(b'') == b''
    assert lzjb_decompress(b'') == b''
    
    # Single byte
    single_byte = b'\x42'
    compressed = lzjb_compress(single_byte)
    assert lzjb_decompress(compressed) == single_byte