def two_sum(nums, target):
    """
    Find two numbers in the given array that add up to the target number.
    
    Args:
        nums (list): A list of integers to search through
        target (int): The target sum to find
    
    Returns:
        list: A list containing the indices of the two numbers that add up to the target.
              Returns an empty list if no such pair is found.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Create a dictionary to store complement values
    num_dict = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            # Return the indices of the two numbers
            return [num_dict[complement], i]
        
        # Store the current number and its index
        num_dict[num] = i
    
    # Return empty list if no solution is found
    return []