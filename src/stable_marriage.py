def gale_shapley_stable_marriage(men_preferences, women_preferences):
    """
    Implement the Gale-Shapley algorithm for stable marriage problem.
    
    Args:
    men_preferences (list of lists): A list where each inner list represents 
        the preference order of men for women (from most to least preferred).
    women_preferences (list of lists): A list where each inner list represents 
        the preference order of women for men (from most to least preferred).
    
    Returns:
    dict: A stable matching where keys are men and values are their matched women.
    
    Raises:
    ValueError: If the number of men and women are not equal or preferences are invalid.
    """
    # Validate input
    if not men_preferences or not women_preferences:
        raise ValueError("Preferences cannot be empty")
    
    n = len(men_preferences)
    if len(women_preferences) != n:
        raise ValueError("Number of men and women must be equal")
    
    # Prepare women's preference rankings
    women_ranking = [{}  for _ in range(n)]
    for w, prefs in enumerate(women_preferences):
        for rank, m in enumerate(prefs):
            women_ranking[w][m] = rank
    
    # Initialize matching
    matching = {}  # men -> women
    women_partners = [None] * n  # women's current partners
    men_proposal_index = [0] * n  # track proposal index for each man
    
    # Continue until all men are matched
    while len(matching) < n:
        # Find unmatched man
        for m in range(n):
            if m not in matching:
                # Get the next woman in this man's preference list
                if men_proposal_index[m] >= n:
                    raise ValueError("No stable matching possible")
                
                w = men_preferences[m][men_proposal_index[m]]
                men_proposal_index[m] += 1
                
                # Check if woman is free
                if women_partners[w] is None:
                    # Match them
                    matching[m] = w
                    women_partners[w] = m
                else:
                    # Check if woman prefers new man
                    current_partner = women_partners[w]
                    
                    # Compare preferences
                    if women_ranking[w][m] < women_ranking[w][current_partner]:
                        # Woman prefers new man
                        del matching[current_partner]
                        matching[m] = w
                        women_partners[w] = m
    
    return matching