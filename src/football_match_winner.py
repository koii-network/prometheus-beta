def determine_football_match_winner(team1_players, team2_players, team1_goals, team2_goals):
    """
    Determine the winner of a football match based on players and goals.
    
    Args:
    team1_players (int): Number of players on team 1
    team2_players (int): Number of players on team 2
    team1_goals (int): Number of goals scored by team 1
    team2_goals (int): Number of goals scored by team 2
    
    Returns:
    str: Winner of the match ('Team 1', 'Team 2', 'Draw')
    
    Raises:
    ValueError: If number of players is invalid (less than or equal to 0)
    """
    # Validate player count
    if team1_players <= 0 or team2_players <= 0:
        raise ValueError("Number of players must be greater than 0")
    
    # Basic goal comparison
    if team1_goals > team2_goals:
        return 'Team 1'
    elif team2_goals > team1_goals:
        return 'Team 2'
    
    # If goals are equal, consider player count
    if team1_players > team2_players:
        return 'Team 1'
    elif team2_players > team1_players:
        return 'Team 2'
    
    # If both goals and player count are equal, it's a draw
    return 'Draw'