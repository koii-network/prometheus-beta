def transform_multi_array(input_array):
    """
    Transform a multi-dimensional array by:
    1. Removing empty sub-arrays
    2. Reversing the order of elements in each sub-array
    3. Flattening the array
    4. Removing duplicates while maintaining original order

    Args:
        input_array (list): A multi-dimensional list to transform

    Returns:
        list: Transformed and cleaned list
    """
    # Remove empty sub-arrays
    non_empty_arrays = [arr for arr in input_array if arr]
    
    # Reverse elements in each sub-array
    reversed_arrays = [arr[::-1] for arr in non_empty_arrays]
    
    # Flatten the array
    flattened_array = [item for sublist in reversed_arrays for item in sublist]
    
    # Remove duplicates while maintaining order
    seen = set()
    result = []
    for item in flattened_array:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result