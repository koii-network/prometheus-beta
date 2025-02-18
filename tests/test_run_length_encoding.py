import pytest
from src.run_length_encoding import run_length_encode, run_length_decode

def test_rle_encoding_string():
    """Test RLE encoding with a string input"""
    input_data = "AABBBCCCC"
    expected = [['A', 2], ['B', 3], ['C', 4]]
    assert run_length_encode(input_data) == expected

def test_rle_encoding_list():
    """Test RLE encoding with a list input"""
    input_data = [1, 1, 2, 2, 2, 3, 3, 3, 3]
    expected = [[1, 2], [2, 3], [3, 4]]
    assert run_length_encode(input_data) == expected

def test_rle_decoding():
    """Test RLE decoding"""
    input_compressed = [['A', 2], ['B', 3], ['C', 4]]
    expected = list('AABBBCCCC')
    assert run_length_decode(input_compressed) == expected

def test_rle_encode_single_character():
    """Test encoding with a single character"""
    input_data = "X"
    expected = [['X', 1]]
    assert run_length_encode(input_data) == expected

def test_rle_decode_single_run():
    """Test decoding a single run"""
    input_compressed = [['Y', 5]]
    expected = ['Y'] * 5
    assert run_length_decode(input_compressed) == expected

def test_rle_encode_empty_input():
    """Test encoding with empty input"""
    with pytest.raises(ValueError):
        run_length_encode("")

def test_rle_decode_empty_input():
    """Test decoding with empty input"""
    with pytest.raises(ValueError):
        run_length_decode([])

def test_rle_encode_invalid_type():
    """Test encoding with invalid input type"""
    with pytest.raises(TypeError):
        run_length_encode(123)

def test_rle_decode_invalid_type():
    """Test decoding with invalid input type"""
    with pytest.raises(TypeError):
        run_length_decode("not a list")

def test_rle_decode_invalid_format():
    """Test decoding with invalid compression format"""
    with pytest.raises(ValueError):
        run_length_decode([['A', -1]])  # Invalid count

def test_round_trip_encode_decode():
    """Test full round trip encoding and decoding"""
    original_data = "HELLO WORLD!!!"
    compressed = run_length_encode(original_data)
    decoded = run_length_decode(compressed)
    assert decoded == list(original_data)