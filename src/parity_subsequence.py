def find_longest_parity_subsequence(nums):
    """
    Find the longest contiguous subsequence with the same parity (all even or all odd).
    
    Args:
        nums (list[int]): Input list of integers
    
    Returns:
        list[int]: The longest contiguous subsequence with consistent parity
    
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
    
    # Track the longest subsequences
    longest_even_subseq = []
    longest_odd_subseq = []
    
    # Current subsequence being built
    current_even_subseq = []
    current_odd_subseq = []
    
    for num in nums:
        is_even = num % 2 == 0
        
        if is_even:
            # Continue or start even subsequence
            current_even_subseq.append(num)
            # Reset odd subsequence
            current_odd_subseq = []
        else:
            # Continue or start odd subsequence
            current_odd_subseq.append(num)
            # Reset even subsequence
            current_even_subseq = []
        
        # Update longest subsequences
        if len(current_even_subseq) > len(longest_even_subseq):
            longest_even_subseq = current_even_subseq.copy()
        
        if len(current_odd_subseq) > len(longest_odd_subseq):
            longest_odd_subseq = current_odd_subseq.copy()
    
    # Return the longer subsequence, preferring even if equal
    return longest_even_subseq if len(longest_even_subseq) >= len(longest_odd_subseq) else longest_odd_subseq