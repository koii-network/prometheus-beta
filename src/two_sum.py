def two_sum(nums, target):
    """
    Find two numbers in the array that add up to the target.
    
    Args:
        nums (list): List of integers to search through
        target (int): The target sum to find
    
    Returns:
        list: Indices of the two numbers that add up to the target, 
              or an empty list if no such pair exists
    """
    # Use a hash map for O(n) time complexity
    num_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            return [num_dict[complement], i]
        
        # Store the current number and its index
        num_dict[num] = i
    
    # If no solution is found
    return []