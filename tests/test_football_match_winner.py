import pytest
from src.football_match_winner import determine_football_match_winner

def test_team1_wins_by_goals():
    assert determine_football_match_winner(11, 11, 3, 1) == 'Team 1'

def test_team2_wins_by_goals():
    assert determine_football_match_winner(11, 11, 1, 3) == 'Team 2'

def test_team1_wins_by_players_when_goals_are_equal():
    assert determine_football_match_winner(11, 10, 2, 2) == 'Team 1'

def test_team2_wins_by_players_when_goals_are_equal():
    assert determine_football_match_winner(10, 11, 2, 2) == 'Team 2'

def test_draw_when_goals_and_players_are_equal():
    assert determine_football_match_winner(11, 11, 2, 2) == 'Draw'

def test_invalid_inputs_negative_numbers():
    with pytest.raises(ValueError, match="Number of players and goals cannot be negative"):
        determine_football_match_winner(-1, 11, 2, 2)

def test_invalid_inputs_non_integers():
    with pytest.raises(ValueError, match="All inputs must be integers"):
        determine_football_match_winner(11, 11, 2.5, 2)

def test_zero_goals_and_players():
    assert determine_football_match_winner(0, 0, 0, 0) == 'Draw'