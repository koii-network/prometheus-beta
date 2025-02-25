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
    
    longest_subsequence = []
    
    for start in range(len(nums)):
        # Check parity of start element
        is_start_even = nums[start] % 2 == 0
        
        # Candidate subsequence 
        current_subsequence = [nums[start]]
        
        # Extend subsequence forward
        for j in range(start + 1, len(nums)):
            # Continue if maintains parity 
            if (is_start_even and nums[j] % 2 == 0) or (not is_start_even and nums[j] % 2 != 0):
                current_subsequence.append(nums[j])
            else:
                break
        
        # Compare to longest subsequence
        if len(current_subsequence) > len(longest_subsequence):
            longest_subsequence = current_subsequence
    
    return longest_subsequence