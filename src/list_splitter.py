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
    
    Time Complexity: O(2^n), where n is the length of the list
    Space Complexity: O(n) due to recursive call stack
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
    
    def can_partition(index, current_sum, total_remaining):
        """
        Recursive helper function to check subset partition with strict requirements.
        
        Args:
            index (int): Current index in the list
            current_sum (int): Current sum of selected elements
            total_remaining (int): Remaining sum to check
        
        Returns:
            bool: True if target sum can be achieved, False otherwise
        """
        # Base cases
        if current_sum == target_sum and total_remaining == target_sum:
            return True
        
        if index >= len(nums):
            return False
        
        # Create two scenarios: include current element or exclude current element
        # Adjust the remaining total accordingly
        return (can_partition(index + 1, current_sum + nums[index], total_remaining - nums[index]) or 
                can_partition(index + 1, current_sum, total_remaining))
    
    return can_partition(0, 0, total_sum)