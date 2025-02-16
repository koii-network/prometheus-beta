def stable_marriage(men_preferences, women_preferences):
    """
    Implement the Gale-Shapley algorithm for the Stable Marriage Problem.
    
    Args:
        men_preferences (list): A list of preference lists for men, 
                                where each list contains women's indices in order of preference.
        women_preferences (list): A list of preference lists for women, 
                                  where each list contains men's indices in order of preference.
    
    Returns:
        list: A stable matching where the index is the man and the value is the matched woman.
    
    Raises:
        ValueError: If the input lists are invalid (different lengths or inconsistent preferences).
    """
    # Validate input
    if not men_preferences or not women_preferences:
        raise ValueError("Preference lists cannot be empty")
    
    if len(men_preferences) != len(women_preferences):
        raise ValueError("Number of men and women must be equal")
    
    n = len(men_preferences)
    
    # Initialize matching and tracking variables
    women_partners = [None] * n  # Women's current partners
    men_next_proposal = [0] * n  # Track next woman to propose to for each man
    free_men = list(range(n))  # Initially all men are free
    
    while free_men:
        # Pick a free man
        man = free_men.pop(0)
        
        # Find the next woman he wants to propose to
        if men_next_proposal[man] >= n:
            # This man has exhausted all his preferences
            continue
        
        woman = men_preferences[man][men_next_proposal[man]]
        men_next_proposal[man] += 1
        
        # Check woman's current situation
        if women_partners[woman] is None:
            # Woman is free, accept proposal
            women_partners[woman] = man
        else:
            # Woman currently has a partner, compare preferences
            current_partner = women_partners[woman]
            
            # Get woman's preference list
            woman_pref_list = women_preferences[woman]
            
            # Check if new man is preferred over current partner
            if woman_pref_list.index(man) < woman_pref_list.index(current_partner):
                # New man is preferred, replace current partner
                women_partners[woman] = man
                free_men.append(current_partner)
            else:
                # Current partner is preferred, man remains free
                free_men.append(man)
    
    return women_partners