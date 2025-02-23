def can_split_list_with_equal_sum(nums):
    """
    Determine if a list of integers can be split into two sublists with equal sum.
    
    Args:
        nums (list): A list of integers to be split.
    
    Returns:
        bool: True if the list can be split into two sublists with equal sum, False otherwise.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains non-integer elements.
    
    Time Complexity: O(n * sum), where n is the length of the list
    Space Complexity: O(sum)
    """
    # Validate input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Handle edge cases
    if not nums or len(nums) < 2:
        return False
    
    # Ensure all elements are integers
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All list elements must be integers")
    
    # If total sum is odd, it can't be split equally
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    # Dynamic programming approach
    # Create a set to track possible subset sums
    possible_sums = {0}
    
    for num in nums:
        # Create a copy to avoid modifying set during iteration
        current_sums = possible_sums.copy()
        
        for existing_sum in current_sums:
            new_sum = existing_sum + num
            
            # If we've found the target sum, return True
            if new_sum == target_sum:
                return True
            
            # If new sum is less than total target, add to possible sums
            if new_sum < total_sum:
                possible_sums.add(new_sum)
    
    return False