def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays with O(log(min(m,n))) time complexity.
    
    Args:
        nums1 (list): First sorted input array
        nums2 (list): Second sorted input array
    
    Returns:
        float: Median of the two sorted arrays
    
    Raises:
        ValueError: If input is not a valid list of numbers or not sorted
    """
    # Validate input 
    if nums1 is None or nums2 is None:
        raise ValueError("Inputs must not be None")
    
    if not isinstance(nums1, list) or not isinstance(nums2, list):
        raise ValueError("Inputs must be lists")
    
    # Check if arrays are sorted
    def is_sorted(arr):
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) if arr else True
    
    if not (is_sorted(nums1) and is_sorted(nums2)):
        raise ValueError("Input arrays must be sorted")
    
    # Ensure first array is the smaller one for efficiency
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    
    while low <= high:
        partition_x = (low + high) // 2
        partition_y = ((m + n + 1) // 2) - partition_x
        
        # Edge cases for finding max and min values
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == m else nums1[partition_x]
        
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == n else nums2[partition_y]
        
        # Check if we have found the correct partition
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            # If total length is odd
            if (m + n) % 2 != 0:
                return max(max_left_x, max_left_y)
            
            # If total length is even
            return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
        
        # Adjust partition
        elif max_left_x > min_right_y:
            high = partition_x - 1
        else:
            low = partition_x + 1
    
    # If no valid partition found
    raise ValueError("Could not find median")