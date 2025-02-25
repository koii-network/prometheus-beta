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
    
    for start in range(len(nums)):
        # Check if starting number is even or odd
        is_start_even = nums[start] % 2 == 0
        
        # Current subsequence
        current_subsequence = [nums[start]]
        
        # Find consecutive subsequence
        for j in range(start + 1, len(nums)):
            # Continue subsequence if parity matches
            if (is_start_even and nums[j] % 2 == 0) or (not is_start_even and nums[j] % 2 != 0):
                current_subsequence.append(nums[j])
            else:
                break
        
        # Update subsequences based on length
        if is_start_even:
            if len(current_subsequence) > len(even_subsequence):
                even_subsequence = current_subsequence
        else:
            if len(current_subsequence) > len(odd_subsequence):
                odd_subsequence = current_subsequence
    
    # Return the longer subsequence (prefer even if equal)
    return even_subsequence if len(even_subsequence) >= len(odd_subsequence) else odd_subsequence