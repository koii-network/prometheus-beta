def find_second_largest(arr):
    """
    Find the second largest element in an array of integers.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The second largest element in the array.

    Raises:
        ValueError: If the input array has fewer than 2 unique elements.
    """
    # Check if input is valid
    if not arr or len(arr) < 2:
        raise ValueError("Input array must contain at least 2 unique elements")

    # Remove duplicates and sort the array in descending order
    unique_sorted = sorted(set(arr), reverse=True)

    # Check if there are at least 2 unique elements
    if len(unique_sorted) < 2:
        raise ValueError("Input array must contain at least 2 unique elements")

    # Return the second element (which is the second largest)
    return unique_sorted[1]