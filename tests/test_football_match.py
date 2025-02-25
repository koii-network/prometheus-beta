import pytest
from src.football_match import determine_football_match_winner

def test_team1_wins_by_goals():
    assert determine_football_match_winner(11, 11, 3, 2) == 'Team 1'

def test_team2_wins_by_goals():
    assert determine_football_match_winner(11, 11, 2, 3) == 'Team 2'

def test_draw_by_goals():
    assert determine_football_match_winner(11, 11, 2, 2) == 'Draw'

def test_team1_wins_by_players():
    assert determine_football_match_winner(12, 11, 2, 2) == 'Team 1'

def test_team2_wins_by_players():
    assert determine_football_match_winner(11, 12, 2, 2) == 'Team 2'

def test_invalid_inputs():
    with pytest.raises(ValueError, match="All inputs must be integers"):
        determine_football_match_winner(11.5, 11, 2, 2)
    
    with pytest.raises(ValueError, match="Inputs cannot be negative"):
        determine_football_match_winner(-1, 11, 2, 2)
    
    with pytest.raises(ValueError, match="Inputs cannot be negative"):
        determine_football_match_winner(11, 11, -1, 2)

def test_zero_inputs():
    assert determine_football_match_winner(0, 0, 0, 0) == 'Draw'

def test_different_zero_goals():
    assert determine_football_match_winner(11, 11, 0, 3) == 'Team 2'