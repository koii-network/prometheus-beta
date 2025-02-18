def stable_marriage(men_preferences, women_preferences):
    """
    Implement the Gale-Shapley algorithm for the Stable Marriage Problem.
    
    Args:
        men_preferences (list of lists): Preference lists for men 
            (each inner list represents a man's ranked preference of women)
        women_preferences (list of lists): Preference lists for women 
            (each inner list represents a woman's ranked preference of men)
    
    Returns:
        dict: A stable matching where keys are men and values are their matched women
    
    Raises:
        ValueError: If the input lists are not of equal length or not valid
    """
    # Input validation
    if not men_preferences or not women_preferences:
        raise ValueError("Preference lists cannot be empty")
    
    if len(men_preferences) != len(women_preferences):
        raise ValueError("Number of men and women must be equal")
    
    n = len(men_preferences)
    
    # Encode women's preferences as a ranking dictionary
    women_rank = [dict() for _ in range(n)]
    for w, pref in enumerate(women_preferences):
        for rank, m in enumerate(pref):
            women_rank[w][m] = rank
    
    # Initialize data structures
    wife = [None] * n  # Each woman's current husband (or None)
    husband = [None] * n  # Each man's current wife (or None)
    
    # Free men stack
    free_men = list(range(n))
    
    while free_men:
        m = free_men.pop(0)
        
        # Find the highest-ranked woman this man hasn't proposed to yet
        for w in men_preferences[m]:
            # If w is free, match her with m
            if wife[w] is None:
                wife[w] = m
                husband[m] = w
                break
            
            # If w prefers m to her current husband
            current_husband = wife[w]
            if women_rank[w][m] < women_rank[w][current_husband]:
                # w breaks up with current husband and matches with m
                husband[current_husband] = None
                free_men.append(current_husband)
                
                wife[w] = m
                husband[m] = w
                break
    
    # Convert to dictionary format for easier return
    return {m: wife[m] for m in range(n)}