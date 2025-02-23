def min_sequence_reconstruction(original, current):
    """
    Determine the minimum number of insertions and removals required to 
    reconstruct the original sequence from the current sequence.
    
    Args:
        original (list): The target original sequence.
        current (list): The current sequence to be transformed.
    
    Returns:
        int: The minimum number of insertions and removals needed.
    
    Raises:
        ValueError: If input is not a list or inputs are None.
    """
    # Validate inputs
    if original is None or current is None:
        raise ValueError("Input sequences cannot be None")
    
    if not isinstance(original, list) or not isinstance(current, list):
        raise ValueError("Inputs must be lists")
    
    # If either list is empty, return the length of the other list
    if not original:
        return len(current)
    if not current:
        return len(original)
    
    # Count element frequencies in both lists
    from collections import Counter
    original_freq = Counter(original)
    current_freq = Counter(current)
    
    # Calculate removals (elements to remove from current)
    removals = 0
    current_copy = current_freq.copy()
    for elem, count in original_freq.items():
        if elem not in current_copy or current_copy[elem] < count:
            # Need to either remove extra elements or add missing elements
            if elem in current_copy:
                removals += current_copy[elem] - count
            else:
                # If element is missing, we'll count it as removal
                removals += current_copy.get(elem, 0)
    
    # Calculate insertions (missing elements)
    insertions = 0
    current_copy = current_freq.copy()
    for elem, count in original_freq.items():
        if elem not in current_copy or current_copy[elem] < count:
            if elem in current_copy:
                insertions += count - current_copy[elem]
            else:
                insertions += count
    
    return removals + insertions