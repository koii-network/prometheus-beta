def determine_football_match_winner(team1_players, team2_players, team1_goals, team2_goals):
    """
    Determine the winner of a football match based on goals scored and player count.
    
    Args:
    team1_players (int): Number of players on team 1
    team2_players (int): Number of players on team 2
    team1_goals (int): Number of goals scored by team 1
    team2_goals (int): Number of goals scored by team 2
    
    Returns:
    str: Winner of the match ('Team 1', 'Team 2', or 'Draw')
    
    Conditions:
    - If one team has more goals, that team wins
    - If goals are equal, it's a draw
    - If a team has less than 7 players, they automatically lose
    """
    # Check for invalid player count
    if team1_players < 7:
        return 'Team 2'
    if team2_players < 7:
        return 'Team 1'
    
    # Compare goals
    if team1_goals > team2_goals:
        return 'Team 1'
    elif team2_goals > team1_goals:
        return 'Team 2'
    else:
        return 'Draw'