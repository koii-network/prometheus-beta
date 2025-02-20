def find_three_sum(arr, target_sum):
    """
    Find all unique triplets in the array that add up to the target sum.
    
    Args:
        arr (list): List of integers to search for triplets
        target_sum (int): The target sum to find triplets for
    
    Returns:
        list: A list of unique triplets that sum to the target
    """
    # Sort the array to help with duplicate elimination and two-pointer technique
    arr.sort()
    triplets = []
    
    # Iterate through the array, fixing one element and using two-pointer technique
    for i in range(len(arr) - 2):
        # Skip duplicates for the first element to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i-1]:
            continue
        
        # Use two pointers to find complementary pairs
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target_sum:
                # Found a triplet
                triplets.append([arr[i], arr[left], arr[right]])
                
                # Skip duplicates for left and right pointers
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                
                # Move pointers inward
                left += 1
                right -= 1
            
            elif current_sum < target_sum:
                # Sum is too small, move left pointer to increase
                left += 1
            
            else:
                # Sum is too large, move right pointer to decrease
                right -= 1
    
    return triplets