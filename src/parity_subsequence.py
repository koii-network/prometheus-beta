def find_longest_parity_subsequence(nums):
    """
    Find the longest subsequence with the same parity (all even or all odd).
    
    Args:
        nums (list[int]): Input list of integers
    
    Returns:
        list[int]: The longest subsequence with consistent parity
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Validate input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # If only one element, return it
    if len(nums) == 1:
        return nums
    
    # Track the longest subsequences for even and odd
    even_subsequence = []
    odd_subsequence = []
    
    # Track the current subsequences being built
    current_even = []
    current_odd = []
    
    for num in nums:
        # Check parity
        is_even = num % 2 == 0
        
        # Build or reset even subsequence
        if is_even:
            current_even.append(num)
            current_odd = []
        else:
            current_odd.append(num)
            current_even = []
        
        # Update longest subsequences
        if len(current_even) > len(even_subsequence):
            even_subsequence = current_even.copy()
        
        if len(current_odd) > len(odd_subsequence):
            odd_subsequence = current_odd.copy()
    
    # Return the longer subsequence
    return even_subsequence if len(even_subsequence) >= len(odd_subsequence) else odd_subsequence