def determine_football_match_winner(team1_players, team2_players, team1_goals, team2_goals):
    """
    Determine the winner of a football match based on goals and players.
    
    Args:
    team1_players (int): Number of players in team 1
    team2_players (int): Number of players in team 2
    team1_goals (int): Number of goals scored by team 1
    team2_goals (int): Number of goals scored by team 2
    
    Returns:
    str: The winner of the match ('Team 1', 'Team 2', or 'Draw')
    
    Conditions:
    1. If one team has more goals, that team wins
    2. If goals are equal, but one team has more players, that team wins
    3. If goals and players are equal, it's a draw
    4. If invalid inputs are provided, raise a ValueError
    """
    # Validate input types
    if not all(isinstance(x, int) for x in [team1_players, team2_players, team1_goals, team2_goals]):
        raise ValueError("All inputs must be integers")
    
    # Validate input ranges
    if any(x < 0 for x in [team1_players, team2_players, team1_goals, team2_goals]):
        raise ValueError("Number of players and goals cannot be negative")
    
    # Check goals
    if team1_goals > team2_goals:
        return 'Team 1'
    elif team2_goals > team1_goals:
        return 'Team 2'
    
    # If goals are equal, check players
    if team1_players > team2_players:
        return 'Team 1'
    elif team2_players > team1_players:
        return 'Team 2'
    
    # If everything is equal, it's a draw
    return 'Draw'