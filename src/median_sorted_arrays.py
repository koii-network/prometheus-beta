def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays.
    
    Args:
        nums1 (list): First sorted input array
        nums2 (list): Second sorted input array
    
    Returns:
        float: Median of the two sorted arrays
    
    Raises:
        ValueError: If input lists are not sorted or contain non-numeric elements
    """
    # Validate inputs are sorted and contain numeric elements
    def is_sorted_numeric(arr):
        return (all(isinstance(x, (int, float)) for x in arr) and 
                all(arr[i] <= arr[i+1] for i in range(len(arr)-1)))
    
    if not (is_sorted_numeric(nums1) and is_sorted_numeric(nums2)):
        raise ValueError("Input arrays must be sorted and contain numeric elements")
    
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
    
    # Add remaining elements
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    
    # Calculate median
    total_length = len(merged)
    mid = total_length // 2
    
    if total_length % 2 == 0:
        # Even number of elements, return average of two middle numbers
        return (merged[mid-1] + merged[mid]) / 2
    else:
        # Odd number of elements, return middle number
        return merged[mid]