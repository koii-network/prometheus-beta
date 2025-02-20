import pytest
from src.football_match_winner import determine_football_match_winner

def test_team1_wins_by_goals():
    assert determine_football_match_winner(11, 11, 3, 1) == 'Team 1'

def test_team2_wins_by_goals():
    assert determine_football_match_winner(11, 11, 1, 3) == 'Team 2'

def test_draw_by_goals():
    assert determine_football_match_winner(11, 11, 2, 2) == 'Draw'

def test_team1_wins_by_player_count():
    assert determine_football_match_winner(12, 11, 2, 2) == 'Team 1'

def test_team2_wins_by_player_count():
    assert determine_football_match_winner(11, 12, 2, 2) == 'Team 2'

def test_invalid_player_count():
    with pytest.raises(ValueError):
        determine_football_match_winner(0, 11, 2, 2)
    
    with pytest.raises(ValueError):
        determine_football_match_winner(11, 0, 2, 2)
    
    with pytest.raises(ValueError):
        determine_football_match_winner(-1, 11, 2, 2)