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
    if not nums:
        return False
    
    # Ensure all elements are integers
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All list elements must be integers")
    
    # If total sum is odd, it can't be split equally
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    def can_achieve_sum(index, current_sum):
        """
        Recursive helper function to check if target sum can be achieved.
        
        Args:
            index (int): Current index in the list
            current_sum (int): Current sum of selected elements
        
        Returns:
            bool: True if target sum can be achieved, False otherwise
        """
        # Base cases
        if current_sum == target_sum:
            return True
        
        if index >= len(nums) or current_sum > target_sum:
            return False
        
        # Try two choices for each element:
        # 1. Include the current element
        # 2. Skip the current element
        return (can_achieve_sum(index + 1, current_sum + nums[index]) or 
                can_achieve_sum(index + 1, current_sum))
    
    return can_achieve_sum(0, 0)