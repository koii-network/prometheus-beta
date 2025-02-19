def tournament_sort(arr):
    """
    Implement tournament sort algorithm.
    
    Tournament sort works by creating a tournament tree (binary heap) 
    and repeatedly extracting the minimum element.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains elements that cannot be compared
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    data = arr.copy()
    n = len(data)
    
    # Create tournament tree (tournament bracket)
    tournament = [None] * (2 * n - 1)
    
    # Fill the leaf nodes with input elements
    for i in range(n):
        tournament[n - 1 + i] = data[i]
    
    # Build the tournament tree from bottom up
    for i in range(n - 2, -1, -1):
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Compare left and right children and select the minimum
        if tournament[left] is not None and tournament[right] is not None:
            tournament[i] = min(tournament[left], tournament[right])
        elif tournament[left] is not None:
            tournament[i] = tournament[left]
        elif tournament[right] is not None:
            tournament[i] = tournament[right]
    
    # Extract elements in sorted order
    sorted_arr = []
    for _ in range(n):
        # Root of tournament tree is the current minimum
        min_val = tournament[0]
        sorted_arr.append(min_val)
        
        # Find the index of the minimum value
        idx = tournament.index(min_val)
        tournament[idx] = None
        
        # Update tournament tree
        while idx > 0:
            parent = (idx - 1) // 2
            left = 2 * parent + 1
            right = 2 * parent + 2
            
            # Recalculate parent node's value
            if tournament[left] is not None and tournament[right] is not None:
                tournament[parent] = min(tournament[left], tournament[right])
            elif tournament[left] is not None:
                tournament[parent] = tournament[left]
            elif tournament[right] is not None:
                tournament[parent] = tournament[right]
            else:
                tournament[parent] = None
            
            idx = parent
    
    return sorted_arr