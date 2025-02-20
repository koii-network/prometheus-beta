def find_longest_parity_subsequence(arr):
    """
    Find the longest subsequence with the same parity (all even or all odd).
    
    Args:
        arr (list): A list of integers
    
    Returns:
        list: The longest subsequence with uniform parity
    """
    if not arr:
        return []
    
    # Helper function to check parity uniformity
    def is_uniform_parity(subseq):
        return all(x % 2 == subseq[0] % 2 for x in subseq)
    
    # Find longest subsequence
    longest_subseq = []
    for start in range(len(arr)):
        for end in range(start, len(arr)):
            current_subseq = arr[start:end+1]
            
            # Update longest subsequence if current is longer and has uniform parity
            if (len(current_subseq) > len(longest_subseq) and 
                is_uniform_parity(current_subseq)):
                longest_subseq = current_subseq
    
    return longest_subseq