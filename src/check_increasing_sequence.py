def is_valid_increasing_sequence(arr):
    """
    Check if the given array is a valid sequence with distinct integers in strictly increasing order.

    Args:
        arr (list): Input list of integers to check

    Returns:
        bool: True if the array is a valid strictly increasing sequence, False otherwise

    Raises:
        TypeError: If input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Empty list or list with single element is considered a valid sequence
    if len(arr) <= 1:
        return True

    # Ensure all elements are integers
    if not all(isinstance(x, int) for x in arr):
        return False

    # Check for strict increasing order and distinct elements
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False

    return True