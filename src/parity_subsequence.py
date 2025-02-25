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
    
    # Find all possible even and odd subsequences
    even_subsequences = []
    odd_subsequences = []
    
    for start in range(len(nums)):
        # Even subsequence candidates
        current_even = []
        # Odd subsequence candidates
        current_odd = []
        
        for j in range(start, len(nums)):
            # Check parity of current number
            if nums[j] % 2 == 0:
                # If we can continue the last subsequence or start a new one
                if not current_even:
                    current_even = [nums[j]]
                else:
                    current_even.append(nums[j])
                    even_subsequences.append(current_even.copy())
            else:
                # If we can continue the last subsequence or start a new one
                if not current_odd:
                    current_odd = [nums[j]]
                else:
                    current_odd.append(nums[j])
                    odd_subsequences.append(current_odd.copy())
    
    # Find the longest subsequences
    max_even = max(even_subsequences, key=len) if even_subsequences else []
    max_odd = max(odd_subsequences, key=len) if odd_subsequences else []
    
    # If equal length, prefer even
    if len(max_even) >= len(max_odd):
        return max_even
    return max_odd