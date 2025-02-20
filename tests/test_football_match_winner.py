import pytest
from src.football_match_winner import determine_football_match_winner

def test_team1_wins_by_goals():
    result = determine_football_match_winner(11, 11, 3, 2)
    assert result == 'Team 1'

def test_team2_wins_by_goals():
    result = determine_football_match_winner(11, 11, 2, 3)
    assert result == 'Team 2'

def test_match_draw():
    result = determine_football_match_winner(11, 11, 2, 2)
    assert result == 'Draw'

def test_team1_forfeits_insufficient_players():
    result = determine_football_match_winner(6, 11, 0, 0)
    assert result == 'Team 2'

def test_team2_forfeits_insufficient_players():
    result = determine_football_match_winner(11, 6, 0, 0)
    assert result == 'Team 1'

def test_invalid_input_type():
    with pytest.raises(ValueError):
        determine_football_match_winner('11', 11, 2, 2)
    with pytest.raises(ValueError):
        determine_football_match_winner(11, '11', 2, 2)
    with pytest.raises(ValueError):
        determine_football_match_winner(11, 11, '2', 2)
    with pytest.raises(ValueError):
        determine_football_match_winner(11, 11, 2, '2')