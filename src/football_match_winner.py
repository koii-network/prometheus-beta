def determine_football_match_winner(team1_players, team2_players, team1_goals, team2_goals):
    """
    Determine the winner of a football match based on goals and players.
    
    Args:
    team1_players (int): Number of players in team 1
    team2_players (int): Number of players in team 2
    team1_goals (int): Number of goals scored by team 1
    team2_goals (int): Number of goals scored by team 2
    
    Returns:
    str: Winner of the match or 'Draw' if conditions are not met
    
    Conditions:
    1. Team with more goals wins
    2. If goals are equal, team with fewer players wins
    3. If both goals and players are equal, it's a draw
    """
    # Validate inputs
    if not all(isinstance(x, int) and x >= 0 for x in [team1_players, team2_players, team1_goals, team2_goals]):
        raise ValueError("All inputs must be non-negative integers")
    
    # Check goals first
    if team1_goals > team2_goals:
        return "Team 1 Wins"
    elif team2_goals > team1_goals:
        return "Team 2 Wins"
    
    # If goals are equal, check number of players
    if team1_players < team2_players:
        return "Team 1 Wins"
    elif team2_players < team1_players:
        return "Team 2 Wins"
    
    # If both goals and players are equal
    return "Draw"