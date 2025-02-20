import pytest
from src.football_match_winner import determine_football_match_winner

def test_team1_wins_by_goals():
    assert determine_football_match_winner(11, 11, 3, 2) == 'Team 1'

def test_team2_wins_by_goals():
    assert determine_football_match_winner(11, 11, 2, 3) == 'Team 2'

def test_draw():
    assert determine_football_match_winner(11, 11, 2, 2) == 'Draw'

def test_team1_loses_by_player_count():
    assert determine_football_match_winner(6, 11, 5, 3) == 'Team 2'

def test_team2_loses_by_player_count():
    assert determine_football_match_winner(11, 6, 3, 5) == 'Team 1'

def test_invalid_inputs():
    with pytest.raises(TypeError):
        determine_football_match_winner('11', '11', '3', '2')

def test_negative_players():
    with pytest.raises(ValueError):
        determine_football_match_winner(-1, 11, 3, 2)