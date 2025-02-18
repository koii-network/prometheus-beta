import pytest
from src.stable_marriage import stable_marriage

def test_basic_stable_marriage():
    """Test a simple stable marriage scenario"""
    men_preferences = [
        [0, 1],  # Man 0's preferences
        [1, 0]   # Man 1's preferences
    ]
    women_preferences = [
        [1, 0],  # Woman 0's preferences 
        [0, 1]   # Woman 1's preferences
    ]
    
    result = stable_marriage(men_preferences, women_preferences)
    
    # Check that the result is a valid matching
    assert len(result) == 2
    assert 0 in result
    assert 1 in result
    assert result[0] != result[1]  # No man married to same woman

def test_larger_stable_marriage():
    """Test a more complex stable marriage scenario"""
    men_preferences = [
        [0, 1, 2],  # Man 0's preferences
        [1, 2, 0],  # Man 1's preferences
        [2, 0, 1]   # Man 2's preferences
    ]
    women_preferences = [
        [1, 0, 2],  # Woman 0's preferences
        [2, 1, 0],  # Woman 1's preferences
        [0, 2, 1]   # Woman 2's preferences
    ]
    
    result = stable_marriage(men_preferences, women_preferences)
    
    # Check that the result is a valid matching
    assert len(result) == 3
    for m in range(3):
        assert m in result

def test_empty_input_error():
    """Test error handling for empty input"""
    with pytest.raises(ValueError, match="Preference lists cannot be empty"):
        stable_marriage([], [])

def test_unequal_length_error():
    """Test error handling for unequal number of men and women"""
    with pytest.raises(ValueError, match="Number of men and women must be equal"):
        stable_marriage([[0, 1]], [[0], [1], [2]])

def test_stability_property():
    """Verify the stability property of the matching"""
    men_preferences = [
        [0, 1, 2],  # Man 0's preferences
        [1, 2, 0],  # Man 1's preferences
        [2, 0, 1]   # Man 2's preferences
    ]
    women_preferences = [
        [1, 0, 2],  # Woman 0's preferences
        [2, 1, 0],  # Woman 1's preferences
        [0, 2, 1]   # Woman 2's preferences
    ]
    
    result = stable_marriage(men_preferences, women_preferences)
    
    # Check stability: No man-woman pair can improve their match
    for m, w in result.items():
        # Check if m would prefer another woman over w
        for alt_w in men_preferences[m]:
            if alt_w == w:
                break
            
            # If m prefers alt_w, check if alt_w prefers m over her current husband
            current_husband = result.inverse().get(alt_w)
            assert not (women_preferences[alt_w].index(m) < 
                        women_preferences[alt_w].index(current_husband))