def can_partition(nums):
    """
    Determine if a list of integers can be partitioned into two subsets with equal sum.
    
    Args:
        nums (list[int]): A list of positive integers
    
    Returns:
        bool: True if the list can be partitioned into two subsets with equal sum, False otherwise
    
    Raises:
        ValueError: If the input list is empty or contains non-positive integers
    
    Time Complexity: O(n * sum(nums))
    Space Complexity: O(sum(nums))
    """
    # Validate input
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    if any(num <= 0 for num in nums):
        raise ValueError("All numbers must be positive integers")
    
    # Calculate total sum
    total_sum = sum(nums)
    
    # If total sum is odd, cannot be partitioned equally
    if total_sum % 2 != 0:
        return False
    
    # Target is half of total sum
    target = total_sum // 2
    
    # Dynamic Programming solution with memoization
    dp = set([0])
    
    for num in nums:
        # Create a copy of current sums to avoid modifying during iteration
        current_sums = dp.copy()
        for cur_sum in current_sums:
            new_sum = cur_sum + num
            if new_sum == target:
                return True
            if new_sum < target:
                dp.add(new_sum)
    
    return False