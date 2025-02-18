import pytest
from src.lz77_compression import LZ77Compressor

def test_lz77_compress_empty_input():
    """Test compression of empty input"""
    compressor = LZ77Compressor()
    assert compressor.compress('') == []
    assert compressor.compress(b'') == []

def test_lz77_compress_single_char():
    """Test compression of a single character"""
    compressor = LZ77Compressor()
    result = compressor.compress('a')
    assert len(result) == 1
    assert result[0][0] == 0  # offset
    assert result[0][1] == 0  # length
    assert result[0][2] == ord('a')  # character

def test_lz77_compression_and_decompression():
    """Test full compression and decompression cycle"""
    compressor = LZ77Compressor()
    
    # Test cases with repetitive patterns
    test_strings = [
        'hello world',
        'aaaabbbbcccc',
        'abcabcabcabc',
        'the quick brown fox jumps over the lazy dog',
        'repeated ' * 10
    ]
    
    for test_string in test_strings:
        # Compress
        compressed = compressor.compress(test_string)
        
        # Decompress
        decompressed = compressor.decompress(compressed).decode('utf-8')
        
        # Verify
        assert decompressed == test_string, f"Failed for input: {test_string}"

def test_lz77_byte_input():
    """Test compression with byte input"""
    compressor = LZ77Compressor()
    byte_input = b'\x00\x01\x02\x03\x00\x01\x02\x03'
    
    # Compress
    compressed = compressor.compress(byte_input)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    # Verify
    assert decompressed == byte_input

def test_lz77_custom_window_size():
    """Test compression with custom window and lookahead buffer sizes"""
    compressor = LZ77Compressor(window_size=128, lookahead_buffer_size=32)
    test_string = 'abcdefghijklmnopqrstuvwxyz' * 5
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed).decode('utf-8')
    
    # Verify
    assert decompressed == test_string