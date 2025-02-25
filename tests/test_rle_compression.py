import pytest
from src.rle_compression import run_length_encode, run_length_decode

def test_run_length_encode_string():
    """Test RLE encoding for a string with repeated characters"""
    input_data = "AABBBCCCC"
    expected = [['A', 2], ['B', 3], ['C', 4]]
    assert run_length_encode(input_data) == expected

def test_run_length_encode_list():
    """Test RLE encoding for a list with repeated elements"""
    input_data = ['a', 'a', 'b', 'b', 'b', 'c']
    expected = [['a', 2], ['b', 3], ['c', 1]]
    assert run_length_encode(input_data) == expected

def test_run_length_encode_single_char():
    """Test RLE encoding for a single character"""
    input_data = "X"
    expected = [['X', 1]]
    assert run_length_encode(input_data) == expected

def test_run_length_encode_error_empty():
    """Test RLE encoding raises error for empty input"""
    with pytest.raises(ValueError):
        run_length_encode("")
    with pytest.raises(ValueError):
        run_length_encode([])

def test_run_length_encode_error_invalid_type():
    """Test RLE encoding raises error for invalid input types"""
    with pytest.raises(TypeError):
        run_length_encode(123)
    with pytest.raises(TypeError):
        run_length_encode(None)

def test_run_length_decode_basic():
    """Test RLE decoding for basic compressed data"""
    input_data = [['A', 2], ['B', 3], ['C', 4]]
    expected = ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
    assert run_length_decode(input_data) == expected

def test_run_length_decode_single_item():
    """Test RLE decoding for a single compressed item"""
    input_data = [['X', 1]]
    expected = ['X']
    assert run_length_decode(input_data) == expected

def test_run_length_decode_empty():
    """Test RLE decoding for empty input"""
    assert run_length_decode([]) == []

def test_run_length_decode_error_invalid_type():
    """Test RLE decoding raises error for invalid input types"""
    with pytest.raises(TypeError):
        run_length_decode("invalid")
    with pytest.raises(TypeError):
        run_length_decode(123)

def test_run_length_decode_error_malformed_data():
    """Test RLE decoding raises error for malformed compressed data"""
    with pytest.raises(ValueError):
        run_length_decode([['A'], ['B', -1]])
    with pytest.raises(ValueError):
        run_length_decode([['A', 'not a number']])

def test_rle_encode_decode_roundtrip():
    """Test complete roundtrip of encoding and decoding"""
    original = "AABBBCCCCDDDDDEEEEE"
    encoded = run_length_encode(original)
    decoded = ''.join(run_length_decode(encoded))
    assert decoded == original