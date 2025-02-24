def find_three_sum_triplets(nums, target):
    """
    Find all unique triplets in the given array that sum up to the target.
    
    Args:
        nums (list): Input list of integers
        target (int): Target sum to find
    
    Returns:
        list: List of unique triplets that sum to the target
    
    Time Complexity: O(n^2)
    Space Complexity: O(1) excluding the output space
    
    Raises:
        TypeError: If input is not a list or target is not an integer
        ValueError: If input list does not contain enough elements
    """
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    if len(nums) < 3:
        raise ValueError("Input list must contain at least 3 elements")
    
    # Sort the array to help with finding triplets
    nums_copy = nums.copy()  # Create a copy to avoid modifying original input
    nums_copy.sort()
    
    # List to store unique triplets
    triplets = []
    
    # Iterate through the array fixing the first element
    for i in range(len(nums_copy) - 2):
        # Skip duplicates for the first element to avoid duplicate triplets
        if i > 0 and nums_copy[i] == nums_copy[i-1]:
            continue
        
        # Two-pointer approach for the remaining two elements
        left = i + 1
        right = len(nums_copy) - 1
        
        while left < right:
            current_sum = nums_copy[i] + nums_copy[left] + nums_copy[right]
            
            if current_sum == target:
                # Found a valid triplet
                triplets.append([nums_copy[i], nums_copy[left], nums_copy[right]])
                
                # Skip duplicates
                while left < right and nums_copy[left] == nums_copy[left + 1]:
                    left += 1
                while left < right and nums_copy[right] == nums_copy[right - 1]:
                    right -= 1
                
                # Move pointers
                left += 1
                right -= 1
            
            elif current_sum < target:
                # Sum is too small, move left pointer
                left += 1
            
            else:
                # Sum is too large, move right pointer
                right -= 1
    
    return triplets