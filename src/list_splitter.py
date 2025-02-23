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
    
    def can_partition(nums, target):
        """
        Recursive helper function to check subset partition.
        
        Args:
            nums (list): Remaining list of numbers
            target (int): Target sum to achieve
        
        Returns:
            bool: True if target sum can be achieved, False otherwise
        """
        if target == 0:
            return True
        
        if not nums or target < 0:
            return False
        
        # Try including or excluding the current number
        return (can_partition(nums[1:], target - nums[0]) or 
                can_partition(nums[1:], target))
    
    # We need to find a subset with sum equal to half the total sum
    return can_partition(nums, target_sum)