import pytest
from src.stable_marriage import stable_marriage

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
    
    result = stable_marriage(men_preferences, women_preferences)
    assert len(result) == 2
    assert result[0] == 1  # Man 0 is matched with Woman 1
    assert result[1] == 0  # Man 1 is matched with Woman 0

def test_three_person_stable_marriage():
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
    
    result = stable_marriage(men_preferences, women_preferences)
    assert len(result) == 3
    # Verify each woman is matched
    assert set(result) == set(range(3))

def test_invalid_input():
    """Test error handling for invalid inputs."""
    # Empty lists
    with pytest.raises(ValueError, match="Preference lists cannot be empty"):
        stable_marriage([], [])
    
    # Mismatched list lengths
    with pytest.raises(ValueError, match="Number of men and women must be equal"):
        stable_marriage([[0, 1]], [[1, 0], [0, 1]])

def test_deterministic_output():
    """Ensure the algorithm produces a consistent stable matching."""
    men_preferences = [
        [0, 1, 2],
        [1, 2, 0],
        [2, 0, 1]
    ]
    women_preferences = [
        [1, 2, 0],
        [2, 0, 1],
        [0, 1, 2]
    ]
    
    # Run multiple times to check consistency
    results = [stable_marriage(men_preferences, women_preferences) for _ in range(3)]
    
    # All results should be the same
    for result in results[1:]:
        assert result == results[0]