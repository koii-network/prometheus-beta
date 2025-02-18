def stable_marriage(men_preferences, women_preferences):
    """
    Implement the Gale-Shapley algorithm for stable marriage problem.
    
    Args:
    men_preferences (list of list): Preferences of men, where each inner list 
                                    represents a man's preference order of women.
    women_preferences (list of list): Preferences of women, where each inner list 
                                      represents a woman's preference order of men.
    
    Returns:
    dict: A stable matching where keys are women and values are their matched men.
    """
    # Number of men/women (assuming equal number)
    n = len(men_preferences)
    
    # Initialize variables
    women_partners = [None] * n  # Current partner for each woman
    men_next_proposal = [0] * n  # Next woman to propose to for each man
    
    # Track whether each man is currently unmatched
    unmatched_men = list(range(n))
    
    # Create preference rankings for women to quickly check preference order
    women_rank = [None] * n
    for w in range(n):
        women_rank[w] = {m: rank for rank, m in enumerate(women_preferences[w])}
    
    # Continue while there are unmatched men
    while unmatched_men:
        # Pick an unmatched man
        m = unmatched_men[0]
        
        # Get the next woman he wants to propose to
        w = men_preferences[m][men_next_proposal[m]]
        men_next_proposal[m] += 1
        
        # If woman is free, match her with the man
        if women_partners[w] is None:
            women_partners[w] = m
            unmatched_men.remove(m)
        else:
            # Check if woman prefers new man over current partner
            current_partner = women_partners[w]
            
            # Compare preferences using pre-computed ranks
            if women_rank[w][m] < women_rank[w][current_partner]:
                # Woman prefers new man, so break current partnership
                women_partners[w] = m
                unmatched_men.remove(m)
                unmatched_men.append(current_partner)
    
    # Convert to dictionary for easier reading
    return {w: women_partners[w] for w in range(n)}