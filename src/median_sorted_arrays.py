def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays.
    
    Args:
        nums1 (list): First sorted array of integers
        nums2 (list): Second sorted array of integers
    
    Returns:
        float: Median of the combined sorted arrays
    
    Raises:
        ValueError: If either input is not a list
    """
    # Validate input types
    if not isinstance(nums1, list) or not isinstance(nums2, list):
        raise ValueError("Inputs must be lists")
    
    # Merge and sort the arrays
    merged = sorted(nums1 + nums2)
    
    # Calculate median
    length = len(merged)
    
    if length == 0:
        raise ValueError("Cannot find median of empty lists")
    
    # If total length is odd, return middle element
    if length % 2 != 0:
        return float(merged[length // 2])
    
    # If total length is even, return average of two middle elements
    mid_right = length // 2
    mid_left = mid_right - 1
    return (merged[mid_left] + merged[mid_right]) / 2.0