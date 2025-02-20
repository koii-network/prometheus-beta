def two_sum(nums, target):
    """
    Find two numbers in the array that add up to the target number.
    
    Args:
        nums (list): A list of integers to search through.
        target (int): The target sum to find.
    
    Returns:
        list: A list containing the indices of the two numbers that add up to the target.
               Returns an empty list if no such pair is found.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Create a dictionary to store complement values and their indices
    complement_dict = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            # Return the indices of the two numbers
            return [complement_dict[complement], i]
        
        # Store the current number and its index
        complement_dict[num] = i
    
    # Return an empty list if no solution is found
    return []