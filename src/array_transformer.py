def transform_array(input_array):
    """
    Transform a multi-dimensional array by:
    1. Removing empty sub-arrays
    2. Reversing the order of elements in each sub-array
    3. Flattening the array
    4. Removing duplicates while maintaining original order

    Args:
        input_array (list): A multi-dimensional list to be transformed

    Returns:
        list: A transformed list with duplicates removed

    Raises:
        TypeError: If input is not a list
    """
    # Validate input is a list
    if not isinstance(input_array, list):
        raise TypeError("Input must be a list")

    # Remove empty sub-arrays and reverse elements in non-empty sub-arrays
    non_empty_reversed = [
        list(reversed(subarray)) 
        for subarray in input_array 
        if subarray  # Remove empty sub-arrays
    ]

    # Flatten the array
    flattened = []
    for subarray in non_empty_reversed:
        flattened.extend(subarray)

    # Remove duplicates while maintaining order
    seen = set()
    deduplicated = []
    for item in flattened:
        if item not in seen:
            deduplicated.append(item)
            seen.add(item)

    return deduplicated