import pytest
from src.run_length_encoding import run_length_encode

def test_rle_basic_string():
    assert run_length_encode("AABBBCCCC") == [['A', 2], ['B', 3], ['C', 4]]

def test_rle_single_char():
    assert run_length_encode("X") == [['X', 1]]

def test_rle_list_input():
    assert run_length_encode(['A', 'A', 'B', 'B', 'B']) == [['A', 2], ['B', 3]]

def test_rle_empty_list():
    with pytest.raises(ValueError):
        run_length_encode([])

def test_rle_empty_string():
    with pytest.raises(ValueError):
        run_length_encode("")

def test_rle_invalid_input():
    with pytest.raises(TypeError):
        run_length_encode(12345)

def test_rle_mixed_list():
    assert run_length_encode(['A', 'A', 'B', 'C', 'C', 'C']) == [['A', 2], ['B', 1], ['C', 3]]