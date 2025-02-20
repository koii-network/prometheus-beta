def determine_football_match_winner(team1_players, team2_players, team1_goals, team2_goals):
    """
    Determine the winner of a football match based on players and goals.
    
    Args:
        team1_players (int): Number of players in team 1
        team2_players (int): Number of players in team 2
        team1_goals (int): Number of goals scored by team 1
        team2_goals (int): Number of goals scored by team 2
    
    Returns:
        str: Winner of the match ('Team 1', 'Team 2', 'Draw')
    
    Conditions:
    1. If a team has fewer than 7 players, they forfeit
    2. If both teams have 7+ players, winner is determined by goals
    3. If goals are equal, it's a draw
    """
    # Validate input types
    if not all(isinstance(x, int) for x in [team1_players, team2_players, team1_goals, team2_goals]):
        raise ValueError("All inputs must be integers")
    
    # Check if either team forfeits due to insufficient players
    if team1_players < 7:
        return 'Team 2'
    if team2_players < 7:
        return 'Team 1'
    
    # Determine winner by goals
    if team1_goals > team2_goals:
        return 'Team 1'
    elif team2_goals > team1_goals:
        return 'Team 2'
    else:
        return 'Draw'