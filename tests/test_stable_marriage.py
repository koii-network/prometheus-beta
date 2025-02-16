import pytest
from src.stable_marriage import gale_shapley_stable_marriage

def test_basic_stable_marriage():
    """Test a simple stable marriage scenario."""
    men_preferences = [
        [0, 1],  # Man 0's preferences 
        [1, 0]   # Man 1's preferences
    ]
    women_preferences = [
        [1, 0],  # Woman 0's preferences
        [0, 1]   # Woman 1's preferences
    ]
    
    result = gale_shapley_stable_marriage(men_preferences, women_preferences)
    
    # Verify the result
    assert len(result) == 2
    assert result[0] == 0
    assert result[1] == 1

def test_larger_stable_marriage():
    """Test a more complex stable marriage scenario."""
    men_preferences = [
        [0, 1, 2],  # Man 0's preferences
        [1, 2, 0],  # Man 1's preferences
        [2, 0, 1]   # Man 2's preferences
    ]
    women_preferences = [
        [1, 2, 0],  # Woman 0's preferences
        [2, 0, 1],  # Woman 1's preferences
        [0, 1, 2]   # Woman 2's preferences
    ]
    
    result = gale_shapley_stable_marriage(men_preferences, women_preferences)
    
    # Verify the result
    assert len(result) == 3
    assert set(result.keys()) == {0, 1, 2}
    assert set(result.values()) == {0, 1, 2}

def test_empty_input_error():
    """Test error handling for empty inputs."""
    with pytest.raises(ValueError, match="Preferences cannot be empty"):
        gale_shapley_stable_marriage([], [])

def test_unequal_input_error():
    """Test error handling for unequal number of men and women."""
    men_preferences = [[0, 1], [1, 0]]
    women_preferences = [[0]]
    
    with pytest.raises(ValueError, match="Number of men and women must be equal"):
        gale_shapley_stable_marriage(men_preferences, women_preferences)

def test_no_stable_matching_possible():
    """Test scenario where no stable matching is possible."""
    # Create preferences that make a stable matching impossible
    men_preferences = [
        [1, 0, 2],
        [0, 2, 1],
        [2, 1, 0]
    ]
    women_preferences = [
        [2, 1, 0],
        [0, 2, 1],
        [1, 0, 2]
    ]
    
    with pytest.raises(ValueError, match="No stable matching possible"):
        gale_shapley_stable_marriage(men_preferences, women_preferences)