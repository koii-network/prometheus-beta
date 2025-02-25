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
    
    # Variables to track overall longest subsequences
    longest_even_subseq = []
    longest_odd_subseq = []
    
    # Iterate through all possible start and end points
    for start in range(len(nums)):
        even_candidates = []
        odd_candidates = []
        
        # Accumulate candidate subsequences from the start
        for j in range(start, len(nums)):
            current_num = nums[j]
            
            # Process even numbers
            if current_num % 2 == 0:
                # If first even, or can continue even sequence
                if not even_candidates or len(even_candidates[-1]) == 0 or \
                   (len(even_candidates[-1]) > 0 and current_num % 2 == even_candidates[-1][-1] % 2):
                    # Append to most recent even subsequence or start a new one
                    if not even_candidates or len(even_candidates[-1]) == 0:
                        even_candidates.append([current_num])
                    else:
                        even_candidates[-1].append(current_num)
                else:
                    # Start a new even subsequence
                    even_candidates.append([current_num])
                
                # Reset any ongoing odd sequence
                if odd_candidates and len(odd_candidates[-1]) > 0:
                    odd_candidates.append([])
            
            # Process odd numbers
            else:
                # If first odd, or can continue odd sequence
                if not odd_candidates or len(odd_candidates[-1]) == 0 or \
                   (len(odd_candidates[-1]) > 0 and current_num % 2 == odd_candidates[-1][-1] % 2):
                    # Append to most recent odd subsequence or start a new one
                    if not odd_candidates or len(odd_candidates[-1]) == 0:
                        odd_candidates.append([current_num])
                    else:
                        odd_candidates[-1].append(current_num)
                
                # Reset any ongoing even sequence
                if even_candidates and len(even_candidates[-1]) > 0:
                    even_candidates.append([])
        
        # Find the longest even and odd subsequences
        max_even_length = max(len(subseq) for subseq in even_candidates) if even_candidates else 0
        max_odd_length = max(len(subseq) for subseq in odd_candidates) if odd_candidates else 0
        
        # Update overall longest subsequences
        for subseq in even_candidates:
            if len(subseq) == max_even_length and len(subseq) > len(longest_even_subseq):
                longest_even_subseq = subseq
        
        for subseq in odd_candidates:
            if len(subseq) == max_odd_length and len(subseq) > len(longest_odd_subseq):
                longest_odd_subseq = subseq
    
    # Return the longer subsequence, preferring even if equal
    return longest_even_subseq if len(longest_even_subseq) >= len(longest_odd_subseq) else longest_odd_subseq