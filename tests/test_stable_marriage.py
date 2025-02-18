import pytest
from src.stable_marriage import stable_marriage

def test_basic_stable_marriage():
    men_preferences = [
        ["A", "B", "C"],
        ["B", "C", "A"],
        ["C", "A", "B"]
    ]
    women_preferences = [
        ["Y", "Z", "X"],
        ["Z", "X", "Y"],
        ["X", "Y", "Z"]
    ]
    
    result = stable_marriage(men_preferences, women_preferences)
    
    # Verify all men are matched
    assert len(result) == 3
    assert set(result.keys()) == set([m[0] for m in men_preferences])
    assert len(set(result.values())) == 3

def test_single_pair():
    men_preferences = [["A"]]
    women_preferences = [["X"]]
    
    result = stable_marriage(men_preferences, women_preferences)
    
    assert result == {"A": "X"}

def test_empty_input_raises_error():
    with pytest.raises(ValueError, match="Preference lists cannot be empty"):
        stable_marriage([], [])

def test_unbalanced_input_raises_error():
    with pytest.raises(ValueError, match="Number of men and women must be equal"):
        stable_marriage([["A", "B"]], [["X"]])

def test_stability_property():
    men_preferences = [
        ["A", "B", "C"],
        ["B", "C", "A"],
        ["C", "A", "B"]
    ]
    women_preferences = [
        ["Y", "Z", "X"],
        ["Z", "X", "Y"],
        ["X", "Y", "Z"]
    ]
    
    result = stable_marriage(men_preferences, women_preferences)
    
    # Check stability: No man-woman pair would prefer each other over current matches
    for man, matched_woman in result.items():
        man_index = [m[0] for m in men_preferences].index(man)
        woman_index = women_preferences.index([w[0] for w in women_preferences if w[0] == matched_woman][0])
        
        # Check man's preference list
        man_preference_list = men_preferences[man_index]
        for potential_woman in man_preference_list[man_preference_list.index(matched_woman)+1:]:
            # Check if the potential woman prefers this man over her current match
            current_woman_match = [m for m, w in result.items() if w == potential_woman][0]
            potential_woman_index = women_preferences.index([w[0] for w in women_preferences if w[0] == potential_woman][0])
            
            current_match_rank = women_preferences[potential_woman_index].index(current_woman_match)
            proposed_man_rank = women_preferences[potential_woman_index].index(man)
            
            assert proposed_man_rank > current_match_rank, f"Unstable match between {man} and {potential_woman}"