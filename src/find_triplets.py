def find_triplets_with_sum(arr, target_sum):
    """
    Find all unique triplets in the array that sum up to the target sum.
    
    Args:
        arr (list): Input list of integers
        target_sum (int): Target sum to find triplets for
    
    Returns:
        list: List of unique triplets that sum up to target_sum
    """
    # Sort the array to help with optimization and avoiding duplicates
    arr.sort()
    result = []
    n = len(arr)
    
    # Iterate through the array, fixing one element and using two-pointer technique
    for i in range(n - 2):
        # Skip duplicates to avoid repeated triplets
        if i > 0 and arr[i] == arr[i-1]:
            continue
        
        # Use two pointers: one from left and one from right
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target_sum:
                # Found a triplet
                result.append([arr[i], arr[left], arr[right]])
                
                # Skip duplicates
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                
                # Move pointers
                left += 1
                right -= 1
            
            elif current_sum < target_sum:
                # Need a larger sum, move left pointer
                left += 1
            
            else:
                # Need a smaller sum, move right pointer
                right -= 1
    
    return result