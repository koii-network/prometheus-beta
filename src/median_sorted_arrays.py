def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays.
    
    This function implements a solution with O(log(min(m,n))) time complexity.
    
    Args:
        nums1 (List[int]): First sorted input array
        nums2 (List[int]): Second sorted input array
    
    Returns:
        float: Median of the two sorted arrays
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input lists are not sorted
    
    Examples:
        >>> find_median_sorted_arrays([1, 3], [2])
        2.0
        >>> find_median_sorted_arrays([1, 2], [3, 4])
        2.5
    """
    # Validate input
    if not isinstance(nums1, list) or not isinstance(nums2, list):
        raise TypeError("Inputs must be lists")
    
    # Ensure nums1 is the smaller array for efficiency
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    # Check if lists are sorted
    if not all(nums1[i] <= nums1[i+1] for i in range(len(nums1)-1)) or \
       not all(nums2[i] <= nums2[i+1] for i in range(len(nums2)-1)):
        raise ValueError("Input arrays must be sorted")
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        partitionX = (left + right) // 2
        partitionY = (m + n + 1) // 2 - partitionX
        
        # Handle edge cases for max and min of partitions
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]
        
        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]
        
        # Check if we have found the correct partition
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # If total length is even
            if (m + n) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            # If total length is odd
            else:
                return float(max(maxLeftX, maxLeftY))
        
        # Adjust partitions
        elif maxLeftX > minRightY:
            right = partitionX - 1
        else:
            left = partitionX + 1
    
    # If no valid partition is found
    raise ValueError("Unable to find median")