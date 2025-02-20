def process_multi_dimensional_array(arr):
    """
    Process a multi-dimensional array with the following steps:
    1. Remove empty sub-arrays
    2. Reverse the order of elements in each sub-array
    3. Flatten the array
    4. Remove duplicates while maintaining original order

    Args:
        arr (list): A multi-dimensional array to process

    Returns:
        list: Processed array with duplicates removed
    """
    # Remove empty sub-arrays
    non_empty_arrays = [subarray for subarray in arr if subarray]
    
    # Reverse the order of elements in each sub-array
    reversed_arrays = [list(reversed(subarray)) for subarray in non_empty_arrays]
    
    # Flatten the array
    flattened = [item for subarray in reversed_arrays for item in subarray]
    
    # Remove duplicates while maintaining order
    seen = set()
    result = []
    for item in flattened:
        if item not in seen:
            result.append(item)
            seen.add(item)
    
    return result