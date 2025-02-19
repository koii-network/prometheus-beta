def tournament_sort(arr):
    """
    Implement the tournament sort algorithm.
    
    Tournament sort is a sorting algorithm that uses a tournament tree (binary heap)
    to efficiently find the minimum element in each pass.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains elements that cannot be compared
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    unsorted = arr.copy()
    sorted_arr = []
    
    # If list is empty, return empty list
    if not unsorted:
        return sorted_arr
    
    # Tournament sort algorithm
    while unsorted:
        # Create tournament tree (using a list to represent the tree)
        tournament = [None] * (2 * len(unsorted) - 1)
        
        # Fill the leaf nodes
        for i in range(len(unsorted)):
            tournament[len(unsorted) - 1 + i] = unsorted[i]
        
        # Create tournament tree by comparing nodes
        for i in range(len(unsorted) - 2, -1, -1):
            left = 2 * i + 1
            right = 2 * i + 2
            
            # Compare left and right children and select winner
            if tournament[left] is not None and tournament[right] is not None:
                tournament[i] = min(tournament[left], tournament[right])
            elif tournament[left] is not None:
                tournament[i] = tournament[left]
            elif tournament[right] is not None:
                tournament[i] = tournament[right]
        
        # The root of the tournament tree is the minimum element
        winner = tournament[0]
        sorted_arr.append(winner)
        
        # Remove the winner from unsorted list
        unsorted.remove(winner)
    
    return sorted_arr