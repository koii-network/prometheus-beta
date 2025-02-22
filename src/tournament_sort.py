def tournament_sort(arr):
    """
    Implement tournament sort algorithm.
    
    Tournament sort is a sorting algorithm that uses a tournament tree (binary heap)
    to sort elements efficiently.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    """
    # Create a copy of the input list to avoid modifying the original
    input_list = arr.copy()
    
    # Handle empty or single-element lists
    if len(input_list) <= 1:
        return input_list
    
    # Create a tournament tree (binary heap)
    def create_tournament_tree(elements):
        # If only one element, return it
        if len(elements) == 1:
            return elements[0]
        
        # If two elements, return the smaller one
        if len(elements) == 2:
            return min(elements[0], elements[1])
        
        # Divide the elements into two halves
        mid = len(elements) // 2
        left = elements[:mid]
        right = elements[mid:]
        
        # Recursively create tournament subtrees
        left_winner = create_tournament_tree(left)
        right_winner = create_tournament_tree(right)
        
        # Return the winner (smaller element)
        return min(left_winner, right_winner)
    
    # Sorted output list
    sorted_list = []
    
    # Continue until all elements are sorted
    while input_list:
        # Find the tournament winner (smallest element)
        winner = create_tournament_tree(input_list)
        
        # Add winner to sorted list
        sorted_list.append(winner)
        
        # Remove the winner from input list
        input_list.remove(winner)
    
    return sorted_list