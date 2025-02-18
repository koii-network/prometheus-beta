import pytest
from src.stable_marriage import stable_marriage

def test_basic_stable_marriage():
    """Test a simple stable marriage matching."""
    men_preferences = [
        [1, 0],  # Man 0's preferences
        [0, 1]   # Man 1's preferences
    ]
    women_preferences = [
        [1, 0],  # Woman 0's preferences
        [0, 1]   # Woman 1's preferences
    ]
    
    result = stable_marriage(men_preferences, women_preferences)
    assert result == {0: 1, 1: 0}

def test_more_complex_stable_marriage():
    """Test a more complex stable marriage scenario."""
    men_preferences = [
        [1, 0, 2],  # Man 0's preferences
        [2, 0, 1],  # Man 1's preferences
        [0, 1, 2]   # Man 2's preferences
    ]
    women_preferences = [
        [1, 0, 2],  # Woman 0's preferences
        [2, 1, 0],  # Woman 1's preferences
        [0, 1, 2]   # Woman 2's preferences
    ]
    
    result = stable_marriage(men_preferences, women_preferences)
    assert len(result) == 3
    assert set(result.keys()) == {0, 1, 2}
    assert set(result.values()) == {0, 1, 2}

def test_invalid_input():
    """Test error handling for invalid inputs."""
    # Empty lists
    with pytest.raises(ValueError):
        stable_marriage([], [])
    
    # Mismatched list lengths
    with pytest.raises(ValueError):
        stable_marriage([[0, 1]], [[1, 0], [0, 1]])
    
    # Invalid preference lists
    with pytest.raises(ValueError):
        stable_marriage([[0, 1]], [[1, 2]])

def test_preference_list_validation():
    """Test validation of preference list contents."""
    # Repeated preferences
    with pytest.raises(ValueError):
        stable_marriage([[0, 0]], [[1, 1]])
    
    # Incomplete preferences
    with pytest.raises(ValueError):
        stable_marriage([[0]], [[1, 0]])

def test_stability_property():
    """Verify the stability of the matching."""
    men_preferences = [
        [1, 0, 2],  # Man 0's preferences
        [2, 0, 1],  # Man 1's preferences
        [0, 1, 2]   # Man 2's preferences
    ]
    women_preferences = [
        [1, 0, 2],  # Woman 0's preferences
        [2, 1, 0],  # Woman 1's preferences
        [0, 1, 2]   # Woman 2's preferences
    ]
    
    result = stable_marriage(men_preferences, women_preferences)
    
    # Check stability: No man and woman prefer each other over their current partners
    for man, woman in result.items():
        man_pref_list = men_preferences[man]
        woman_pref_list = women_preferences[woman]
        
        # Current ranking of current partner
        current_woman_rank = man_pref_list.index(woman)
        current_man_rank = woman_pref_list.index(man)
        
        # Check against other possible partners
        for other_woman in man_pref_list[:current_woman_rank]:
            other_woman_index = men_preferences[man].index(other_woman)
            other_woman_current_partner = result.inverse()[other_woman] if other_woman in result.inverse() else None
            
            if other_woman_current_partner is not None:
                woman_pref_list = women_preferences[other_woman]
                other_woman_partner_rank = woman_pref_list.index(other_woman_current_partner)
                
                # Verify no improving pair exists
                assert woman_pref_list.index(man) >= other_woman_partner_rank