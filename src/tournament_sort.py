def tournament_sort(arr):
    """
    Implement the tournament sort algorithm.
    
    Tournament sort is a sorting algorithm that uses a tournament tree (binary heap)
    to sort an array of elements efficiently.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy of the input list to avoid modifying the original
    elements = arr.copy()
    n = len(elements)
    
    # Create the tournament tree
    tournament = [None] * (2 * n - 1)
    
    # Fill the leaf nodes with original elements
    for i in range(n):
        tournament[n - 1 + i] = elements[i]
    
    # Build the tournament tree from bottom up
    for i in range(n - 2, -1, -1):
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Compare and set the winner
        if tournament[left] is not None and tournament[right] is not None:
            tournament[i] = min(tournament[left], tournament[right])
        elif tournament[left] is not None:
            tournament[i] = tournament[left]
        elif tournament[right] is not None:
            tournament[i] = tournament[right]
    
    # Sort the array using the tournament tree
    sorted_arr = []
    for _ in range(n):
        # Get the minimum (root) element
        winner = tournament[0]
        sorted_arr.append(winner)
        
        # Find and remove the winner from the tournament tree
        current_index = tournament.index(winner)
        tournament[current_index] = None
        
        # Propagate nulls up the tree
        parent = (current_index - 1) // 2
        while parent >= 0:
            left = 2 * parent + 1
            right = 2 * parent + 2
            
            # Determine the new winner of the current subtree
            if tournament[left] is not None and tournament[right] is not None:
                tournament[parent] = min(tournament[left], tournament[right])
            elif tournament[left] is not None:
                tournament[parent] = tournament[left]
            elif tournament[right] is not None:
                tournament[parent] = tournament[right]
            else:
                tournament[parent] = None
            
            # Move up the tree
            current_index = parent
            parent = (current_index - 1) // 2
    
    return sorted_arr