def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays in O(log(min(m,n))) time complexity.
    
    Args:
        nums1 (list): First sorted input array
        nums2 (list): Second sorted input array
    
    Returns:
        float: Median of the two sorted arrays
    
    Raises:
        ValueError: If input arrays are not sorted or empty
    """
    # Validate input
    if not nums1 and not nums2:
        raise ValueError("Both input arrays cannot be empty")
    
    # Ensure nums1 is the smaller array for efficiency
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        # Partition both arrays
        partition_x = (left + right) // 2
        partition_y = (m + n + 1) // 2 - partition_x
        
        # Find max and min values for partitions
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == m else nums1[partition_x]
        
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == n else nums2[partition_y]
        
        # Check if we have found the correct partition
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            # If total length is even
            if (m + n) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            
            # If total length is odd
            return max(max_left_x, max_left_y)
        
        # Adjust partition
        elif max_left_x > min_right_y:
            right = partition_x - 1
        else:
            left = partition_x + 1
    
    # If no valid partition found
    raise ValueError("Input arrays are not sorted")