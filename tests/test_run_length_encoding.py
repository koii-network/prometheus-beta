import pytest
from src.run_length_encoding import run_length_encode

def test_run_length_encode_string():
    assert run_length_encode('AABBBCCCC') == '2A3B4C'
    assert run_length_encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB') == '12W1B12W3B24W1B'
    assert run_length_encode('  ') == '2 '

def test_run_length_encode_list():
    assert run_length_encode(['A', 'A', 'B', 'B', 'B']) == '2A3B'
    assert run_length_encode([1, 1, 1, 2, 2, 3]) == '3A2B1C'

def test_run_length_encode_single_character():
    assert run_length_encode('X') == '1X'
    assert run_length_encode(['Y']) == '1Y'

def test_run_length_encode_error_handling():
    with pytest.raises(TypeError):
        run_length_encode(12345)
    
    with pytest.raises(TypeError):
        run_length_encode(None)
    
    with pytest.raises(ValueError):
        run_length_encode('')
    
    with pytest.raises(ValueError):
        run_length_encode([])