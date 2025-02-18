import pytest
from src.stable_marriage import stable_marriage

def test_simple_stable_marriage():
    # Simple test case with 2 men and 2 women
    men_preferences = [
        [1, 0],  # Man 0's preferences
        [0, 1]   # Man 1's preferences
    ]
    women_preferences = [
        [1, 0],  # Woman 0's preferences
        [0, 1]   # Woman 1's preferences
    ]
    
    result = stable_marriage(men_preferences, women_preferences)
    assert len(result) == 2
    assert 0 in result.values()
    assert 1 in result.values()

def test_larger_stable_marriage():
    # More complex test case with 3 men and 3 women
    men_preferences = [
        [1, 2, 0],  # Man 0's preferences
        [0, 2, 1],  # Man 1's preferences
        [1, 0, 2]   # Man 2's preferences
    ]
    women_preferences = [
        [1, 0, 2],  # Woman 0's preferences
        [2, 1, 0],  # Woman 1's preferences
        [0, 2, 1]   # Woman 2's preferences
    ]
    
    result = stable_marriage(men_preferences, women_preferences)
    assert len(result) == 3
    assert set(result.values()) == set(range(3))

def test_invalid_input():
    # Test with mismatched preference list lengths
    with pytest.raises(IndexError):
        stable_marriage(
            [[1, 0], [0]],  # Unequal men preferences
            [[1, 0], [0, 1]]
        )

def test_input_validation():
    # Test with empty preference lists
    with pytest.raises(IndexError):
        stable_marriage([], [])