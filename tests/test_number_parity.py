import pytest
from src.number_parity import determine_parity

def test_even_numbers():
    assert determine_parity(0) == 'even'
    assert determine_parity(2) == 'even'
    assert determine_parity(100) == 'even'
    assert determine_parity(-4) == 'even'

def test_odd_numbers():
    assert determine_parity(1) == 'odd'
    assert determine_parity(3) == 'odd'
    assert determine_parity(99) == 'odd'
    assert determine_parity(-7) == 'odd'

def test_invalid_input():
    with pytest.raises(TypeError):
        determine_parity(3.14)
    
    with pytest.raises(TypeError):
        determine_parity('42')
    
    with pytest.raises(TypeError):
        determine_parity(None)