def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays.
    
    Args:
        nums1 (list): First sorted input array
        nums2 (list): Second sorted input array
    
    Returns:
        float: Median of the combined sorted arrays
    
    Raises:
        ValueError: If input is not a list or contains non-numeric elements
    """
    # Validate input
    if not (isinstance(nums1, list) and isinstance(nums2, list)):
        raise ValueError("Inputs must be lists")
    
    if not all(isinstance(x, (int, float)) for x in nums1 + nums2):
        raise ValueError("All elements must be numeric")
    
    # Merge the two sorted arrays
    merged = []
    i, j = 0, 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    # Add remaining elements from nums1 or nums2
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    
    # Calculate median
    n = len(merged)
    if n == 0:
        raise ValueError("Cannot calculate median of empty lists")
    
    mid = n // 2
    if n % 2 == 0:
        # Even number of elements, average the two middle values
        return (merged[mid-1] + merged[mid]) / 2
    else:
        # Odd number of elements, return the middle value
        return merged[mid]