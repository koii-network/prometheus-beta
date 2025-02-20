def longest_parity_subsequence(arr):
    """
    Find the longest subsequence with the same parity (all even or all odd).
    
    Args:
        arr (list): A list of integers
    
    Returns:
        list: The longest subsequence with consistent parity
    
    Raises:
        ValueError: If input is not a list or is an empty list
    """
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    if not arr:
        return []
    
    # Track longest even and odd subsequences
    longest_even = []
    longest_odd = []
    
    # Current subsequence candidates
    current_even = []
    current_odd = []
    
    for num in arr:
        if num % 2 == 0:  # Even number
            # Extend current even sequence or start a new one
            current_even.append(num)
            current_odd = []  # Reset odd sequence
            
            # Update longest even sequence if needed
            if len(current_even) > len(longest_even):
                longest_even = current_even.copy()
        
        else:  # Odd number
            # Extend current odd sequence or start a new one
            current_odd.append(num)
            current_even = []  # Reset even sequence
            
            # Update longest odd sequence if needed
            if len(current_odd) > len(longest_odd):
                longest_odd = current_odd.copy()
    
    # Return the longer subsequence
    return longest_even if len(longest_even) >= len(longest_odd) else longest_odd