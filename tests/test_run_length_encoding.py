import pytest
from src.run_length_encoding import run_length_encode, run_length_decode

def test_run_length_encode_string():
    """Test RLE encoding with a string input"""
    input_data = "AAAABBBCCCCC"
    expected = [['A', 4], ['B', 3], ['C', 5]]
    assert run_length_encode(input_data) == expected

def test_run_length_encode_list():
    """Test RLE encoding with a list input"""
    input_data = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C']
    expected = [['A', 4], ['B', 3], ['C', 5]]
    assert run_length_encode(input_data) == expected

def test_run_length_encode_single_char():
    """Test RLE encoding with a single character"""
    input_data = "AAAAA"
    expected = [['A', 5]]
    assert run_length_encode(input_data) == expected

def test_run_length_encode_empty_input():
    """Test RLE encoding with empty input"""
    with pytest.raises(ValueError):
        run_length_encode("")
    with pytest.raises(ValueError):
        run_length_encode([])

def test_run_length_encode_invalid_input():
    """Test RLE encoding with invalid input types"""
    with pytest.raises(TypeError):
        run_length_encode(123)
    with pytest.raises(TypeError):
        run_length_encode(None)

def test_run_length_decode_basic():
    """Test basic RLE decoding"""
    input_data = [['A', 4], ['B', 3], ['C', 5]]
    expected = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C']
    assert run_length_decode(input_data) == expected

def test_run_length_decode_single_group():
    """Test RLE decoding with a single group"""
    input_data = [['X', 3]]
    expected = ['X', 'X', 'X']
    assert run_length_decode(input_data) == expected

def test_run_length_decode_empty_input():
    """Test RLE decoding with empty input"""
    with pytest.raises(ValueError):
        run_length_decode([])

def test_run_length_decode_invalid_input():
    """Test RLE decoding with invalid input"""
    with pytest.raises(TypeError):
        run_length_decode("invalid")
    with pytest.raises(ValueError):
        run_length_decode([1, 2])
    with pytest.raises(ValueError):
        run_length_decode([['A']])
    with pytest.raises(ValueError):
        run_length_decode([['A', 'B']])

def test_rle_encode_decode_roundtrip():
    """Test RLE encoding and decoding round trip"""
    original = "AABBCCDDEEEE"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    assert ''.join(decoded) == original