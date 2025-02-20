def process_multi_dimensional_array(input_array):
    """
    Process a multi-dimensional array with the following steps:
    1. Remove empty sub-arrays
    2. Reverse the order of elements in each sub-array
    3. Flatten the array
    4. Remove duplicates while maintaining original order

    Args:
        input_array (list): A multi-dimensional list to process

    Returns:
        list: Processed and transformed list
    """
    # Remove empty sub-arrays
    non_empty_arrays = [subarray for subarray in input_array if subarray]
    
    # Reverse each sub-array
    reversed_arrays = [subarray[::-1] for subarray in non_empty_arrays]
    
    # Flatten the array
    flattened_array = [item for subarray in reversed_arrays for item in subarray]
    
    # Remove duplicates while maintaining order
    seen = set()
    result = []
    for item in flattened_array:
        if item not in seen:
            result.append(item)
            seen.add(item)
    
    return result