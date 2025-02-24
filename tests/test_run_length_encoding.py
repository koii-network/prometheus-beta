import pytest
from src.run_length_encoding import compress_rle, decompress_rle

def test_compress_rle_basic_string():
    assert compress_rle('AAAABBBCCCCC') == '4A3B5C'
    assert compress_rle('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB') == '12W1B12W3B13W1B'

def test_compress_rle_basic_list():
    assert compress_rle(['A', 'A', 'A', 'A', 'B', 'B', 'C']) == '4A2B1C'

def test_decompress_rle_basic():
    assert decompress_rle('4A3B5C') == 'AAAABBBCCCCC'
    assert decompress_rle('12W1B12W3B13W1B') == 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB'

def test_rle_round_trip():
    original = 'AAAABBBCCCCC'
    compressed = compress_rle(original)
    decompressed = decompress_rle(compressed)
    assert decompressed == original

def test_compress_rle_error_handling():
    with pytest.raises(TypeError):
        compress_rle(12345)
    
    with pytest.raises(ValueError):
        compress_rle('')
    
    with pytest.raises(ValueError):
        compress_rle([])

def test_decompress_rle_error_handling():
    with pytest.raises(TypeError):
        decompress_rle(12345)
    
    with pytest.raises(ValueError):
        decompress_rle('')
    
    with pytest.raises(ValueError):
        decompress_rle('2A3')  # Incomplete or malformed input

def test_single_character():
    assert compress_rle('A') == '1A'
    assert decompress_rle('1A') == 'A'

def test_mixed_input():
    input_list = ['A', 'A', 'B', 'C', 'C', 'C']
    assert compress_rle(input_list) == '2A1B3C'
    assert decompress_rle('2A1B3C') == 'AABCCC'