def determine_football_match_winner(team1_players, team2_players, team1_goals, team2_goals):
    """
    Determine the winner of a football match based on goals and player count.
    
    Args:
        team1_players (int): Number of players on team 1
        team2_players (int): Number of players on team 2
        team1_goals (int): Number of goals scored by team 1
        team2_goals (int): Number of goals scored by team 2
    
    Returns:
        str: Winner of the match ('Team 1', 'Team 2', 'Draw')
    
    Raises:
        ValueError: If any input is negative or not an integer
    """
    # Validate inputs
    if not all(isinstance(x, int) for x in [team1_players, team2_players, team1_goals, team2_goals]):
        raise ValueError("All inputs must be integers")
    
    if any(x < 0 for x in [team1_players, team2_players, team1_goals, team2_goals]):
        raise ValueError("Inputs cannot be negative")
    
    # Check special conditions based on goals and players
    if team1_goals > team2_goals:
        return 'Team 1'
    elif team2_goals > team1_goals:
        return 'Team 2'
    
    # If goals are equal, use player count as a tiebreaker
    if team1_players > team2_players:
        return 'Team 1'
    elif team2_players > team1_players:
        return 'Team 2'
    
    # If both goals and players are equal, it's a draw
    return 'Draw'