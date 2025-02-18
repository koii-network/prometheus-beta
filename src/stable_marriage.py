def stable_marriage(men_preferences, women_preferences):
    """
    Implement the Gale-Shapley algorithm for the Stable Marriage Problem.
    
    Args:
    men_preferences (list of lists): Preference lists for men, where each sublist 
                                     contains women's indices in order of preference.
    women_preferences (list of lists): Preference lists for women, where each sublist 
                                       contains men's indices in order of preference.
    
    Returns:
    dict: A stable matching where keys are men's indices and values are their matched women's indices.
    
    Raises:
    ValueError: If the input lists are not of equal length or have inconsistent preferences.
    """
    # Input validation
    if not men_preferences or not women_preferences:
        raise ValueError("Preference lists cannot be empty")
    
    n = len(men_preferences)
    if len(women_preferences) != n:
        raise ValueError("Men and women preference lists must have the same length")
    
    # Check that preference lists are valid
    for prefs in men_preferences + women_preferences:
        if len(prefs) != n or len(set(prefs)) != n:
            raise ValueError("Invalid preference lists")
    
    # Initialize data structures
    women_partners = [None] * n  # Current partner for each woman
    men_partners = [None] * n    # Current partner for each man
    men_next_proposal = [0] * n  # Next woman to propose to for each man
    
    # Tracking women's preference rankings 
    women_rankings = [
        {man: rank for rank, man in enumerate(prefs)} 
        for prefs in women_preferences
    ]
    
    # Continue while there are unmatched men
    while None in men_partners:
        # Find an unmatched man
        proposer = men_partners.index(None)
        
        # Get the next woman he wants to propose to
        proposed_to = men_preferences[proposer][men_next_proposal[proposer]]
        men_next_proposal[proposer] += 1
        
        # If woman is unmatched, they get matched
        if women_partners[proposed_to] is None:
            women_partners[proposed_to] = proposer
            men_partners[proposer] = proposed_to
        else:
            # Current partner of the woman
            current_partner = women_partners[proposed_to]
            
            # Compare the two men based on woman's preferences
            if women_rankings[proposed_to][proposer] < women_rankings[proposed_to][current_partner]:
                # Woman prefers the new man
                women_partners[proposed_to] = proposer
                men_partners[proposer] = proposed_to
                
                # Previous partner is now unmatched
                men_partners[current_partner] = None
    
    # Convert to dictionary for clarity
    return {man: partner for man, partner in enumerate(men_partners)}