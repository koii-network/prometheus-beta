import pytest
from src.lzjh_compression import lzjh_compress, lzjh_decompress

def test_lzjh_compression_decompression_cycle():
    """Test a full compression and decompression cycle"""
    inputs = [
        "ABABABABABABABAB",
        "Hello, world!",
        "こんにちは、世界",
        b'\x01\x02\x03\x01\x02\x03',
        ""
    ]
    
    for input_data in inputs:
        # Compress
        compressed = lzjh_compress(input_data)
        
        # Ensure some compression or at least byte representation
        if isinstance(input_data, str):
            assert len(compressed) <= len(input_data.encode('utf-8'))
        else:
            assert len(compressed) <= len(input_data)
        
        # Decompress
        decompressed = lzjh_decompress(compressed)
        
        # Ensure restoration of original data
        if isinstance(input_data, str):
            assert decompressed.decode('utf-8') == input_data
        else:
            assert decompressed == input_data

def test_lzjh_compress_repeated_patterns():
    """Test compression of repeated patterns"""
    test_cases = [
        "HAHAHAHAHAHAHAHA",
        "ABCABCABCABCABC",
        "111222333444555"
    ]
    
    for input_data in test_cases:
        compressed = lzjh_compress(input_data)
        assert len(compressed) < len(input_data)

def test_lzjh_error_handling():
    """Test error handling for invalid input"""
    with pytest.raises(TypeError):
        lzjh_compress(None)
    
    with pytest.raises(ValueError):
        # Test decompression with invalid code
        lzjh_decompress([300000])  # Impossibly large code

def test_edge_cases():
    """Test various edge cases"""
    # Single character
    single_char = "A"
    compressed = lzjh_compress(single_char)
    assert compressed == [ord('A')]
    
    # Very long repeated sequence
    long_repeat = "X" * 1000
    compressed = lzjh_compress(long_repeat)
    assert len(compressed) < len(long_repeat)