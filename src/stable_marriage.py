def stable_marriage(men_preferences, women_preferences):
    """
    Implement the Gale-Shapley algorithm for the Stable Marriage Problem.
    
    Args:
    men_preferences (list of lists): Preference lists for men, where each sublist 
                                     contains women's names in order of preference
    women_preferences (list of lists): Preference lists for women, where each sublist 
                                       contains men's names ranked by preference
    
    Returns:
    dict: A stable matching where keys are men and values are their matched partners
    
    Raises:
    ValueError: If the input lists are not balanced or empty
    """
    # Validate input
    if not men_preferences or not women_preferences:
        raise ValueError("Preference lists cannot be empty")
    
    if len(men_preferences) != len(women_preferences):
        raise ValueError("Number of men and women must be equal")
    
    # Convert preference lists to indices for efficient lookup
    n = len(men_preferences)
    men_pref_indices = [{woman: rank for rank, woman in enumerate(pref)} for pref in men_preferences]
    women_pref_indices = [{man: rank for rank, man in enumerate(pref)} for pref in women_preferences]
    
    # Initialize matching
    matches = {}
    men_partner = [None] * n
    women_partner = [None] * n
    
    # Track proposal attempts for each man
    men_next_proposal = [0] * n
    
    # Continue until all men are matched
    while None in men_partner:
        # Find an unmatched man
        proposer_index = men_partner.index(None)
        
        # Get the woman he wants to propose to next
        proposed_woman_name = men_preferences[proposer_index][men_next_proposal[proposer_index]]
        proposed_woman_index = women_preferences.index(
            [w for w in women_preferences if w[0] == proposed_woman_name][0]
        )
        
        # Increment next proposal index
        men_next_proposal[proposer_index] += 1
        
        # Check if woman is unmatched
        if women_partner[proposed_woman_index] is None:
            # Match them
            men_partner[proposer_index] = proposed_woman_name
            women_partner[proposed_woman_index] = men_preferences[proposer_index][0]
        else:
            # Woman is already matched, compare preferences
            current_partner_name = women_partner[proposed_woman_index]
            current_partner_index = men_preferences.index(
                [m for m in men_preferences if m[0] == current_partner_name][0]
            )
            
            # Check woman's preference
            current_rank = women_pref_indices[proposed_woman_index][current_partner_name]
            new_rank = women_pref_indices[proposed_woman_index][men_preferences[proposer_index][0]]
            
            if new_rank < current_rank:
                # Woman prefers new man
                men_partner[proposer_index] = proposed_woman_name
                women_partner[proposed_woman_index] = men_preferences[proposer_index][0]
                
                # Previous partner becomes unmatched
                men_partner[current_partner_index] = None
    
    # Create final matching dictionary
    return dict(zip([men[0] for men in men_preferences], men_partner))