def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays.
    
    Args:
        nums1 (list): First sorted array of integers
        nums2 (list): Second sorted array of integers
    
    Returns:
        float: Median of the two sorted arrays
    
    Raises:
        ValueError: If input arrays are not valid (non-list, non-numeric, or both empty)
    """
    # Validate input
    if not (isinstance(nums1, list) and isinstance(nums2, list)):
        raise ValueError("Input must be lists")
    
    # Check if both lists are empty
    if len(nums1) == 0 and len(nums2) == 0:
        raise ValueError("At least one input array must have elements")
    
    # Check if all elements are numeric
    if not (all(isinstance(x, (int, float)) for x in nums1) and 
            all(isinstance(x, (int, float)) for x in nums2)):
        raise ValueError("All array elements must be numeric")
    
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
    if n % 2 == 0:
        # If even number of elements, average the two middle elements
        return (merged[n//2 - 1] + merged[n//2]) / 2
    else:
        # If odd number of elements, return the middle element
        return merged[n//2]