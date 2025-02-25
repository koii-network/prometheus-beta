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
    
    # Track the best subsequences
    longest_even_subsequence = []
    longest_odd_subsequence = []
    
    # Iterate through all possible start positions to handle non-contiguous subsequent elements
    for start in range(len(nums)):
        # Start subsequences from current point, tracking parity
        even_subsequence = []
        odd_subsequence = []
        
        # Iterate through the list from the start point
        for j in range(start, len(nums)):
            # Check parity of current number
            is_even = nums[j] % 2 == 0
            
            # Add to appropriate subsequence
            if is_even:
                even_subsequence.append(nums[j])
                # Clear odd subsequence if it breaks parity
                if odd_subsequence and len(odd_subsequence) == 1:
                    odd_subsequence = []
            else:
                odd_subsequence.append(nums[j])
                # Clear even subsequence if it breaks parity
                if even_subsequence and len(even_subsequence) == 1:
                    even_subsequence = []
        
        # Update longest subsequences, giving preference to even if equal
        if len(even_subsequence) > len(longest_even_subsequence):
            longest_even_subsequence = even_subsequence
        
        if len(odd_subsequence) > len(longest_odd_subsequence):
            longest_odd_subsequence = odd_subsequence
    
    # Return the longer subsequence, preferring even
    return longest_even_subsequence if len(longest_even_subsequence) >= len(longest_odd_subsequence) else longest_odd_subsequence