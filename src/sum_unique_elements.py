def sum_unique_elements(arr):
    """
    Calculate the sum of unique elements in the given array.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Sum of unique elements
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Use a dictionary to track element counts and compute unique sum
    unique_sum = 0
    seen = {}
    
    for num in arr:
        # If we haven't seen this number before or it's the first duplicate
        if num not in seen:
            seen[num] = 1
            unique_sum += num
        # If it's a second or subsequent occurrence, remove from unique sum
        elif seen[num] == 1:
            unique_sum -= num
            seen[num] += 1
    
    return unique_sum