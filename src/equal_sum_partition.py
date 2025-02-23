def can_partition_into_equal_sum_sublists(nums):
    """
    Determine if a list of integers can be split into two sublists with equal sum.
    
    Args:
        nums (list): A list of integers to be partitioned.
    
    Returns:
        bool: True if the list can be split into two sublists with equal sum, False otherwise.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    # Validate input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Check if list contains only integers
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("List must contain only integers")
    
    # Handle empty or single-element list cases
    if len(nums) < 2:
        return False
    
    total_sum = sum(nums)
    
    # If total sum is odd, equal partition is impossible
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    def can_achieve_sum(index, current_sum):
        """
        Recursive helper function to check if target sum can be achieved.
        
        Args:
            index (int): Current index in the list.
            current_sum (int): Current running sum.
        
        Returns:
            bool: True if target sum can be achieved, False otherwise.
        """
        # Base cases
        if current_sum == target_sum:
            return True
        
        if index >= len(nums) or current_sum > target_sum:
            return False
        
        # Try two possibilities:
        # 1. Include current number in the subset
        # 2. Exclude current number from the subset
        return (can_achieve_sum(index + 1, current_sum + nums[index]) or 
                can_achieve_sum(index + 1, current_sum))
    
    return can_achieve_sum(0, 0)