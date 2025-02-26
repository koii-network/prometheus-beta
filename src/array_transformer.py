def _flatten(arr):
    """
    Recursively flatten a nested list.

    Args:
        arr (list): A potentially nested list

    Returns:
        list: A completely flattened list
    """
    flattened = []
    for item in arr:
        if isinstance(item, list):
            flattened.extend(_flatten(item))
        else:
            flattened.append(item)
    return flattened

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

    # Flatten the array (handling nested lists)
    flattened = _flatten(non_empty_reversed)

    # Remove duplicates while maintaining order
    seen = set()
    deduplicated = []
    for item in flattened:
        hashable_item = item if isinstance(item, (int, str, float, bool, tuple)) else str(item)
        if hashable_item not in seen:
            deduplicated.append(item)
            seen.add(hashable_item)

    return deduplicated