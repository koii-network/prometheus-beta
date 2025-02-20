import pytest
from src.football_match_winner import determine_football_match_winner

def test_team1_wins_by_goals():
    assert determine_football_match_winner(11, 11, 3, 2) == "Team 1 Wins"

def test_team2_wins_by_goals():
    assert determine_football_match_winner(11, 11, 2, 3) == "Team 2 Wins"

def test_team1_wins_by_fewer_players():
    assert determine_football_match_winner(10, 11, 2, 2) == "Team 1 Wins"

def test_team2_wins_by_fewer_players():
    assert determine_football_match_winner(11, 10, 2, 2) == "Team 2 Wins"

def test_draw_equal_goals_and_players():
    assert determine_football_match_winner(11, 11, 2, 2) == "Draw"

def test_invalid_negative_input():
    with pytest.raises(ValueError):
        determine_football_match_winner(-1, 11, 2, 2)

def test_invalid_non_integer_input():
    with pytest.raises(ValueError):
        determine_football_match_winner(11, 11, 2.5, 2)