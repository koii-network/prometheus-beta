def insertion_sort(arr):
    """
    Implements the insertion sort algorithm to sort a list in-place.

    Args:
        arr (list): The input list to be sorted.

    Returns:
        list: The sorted list.

    Raises:
        TypeError: If the input is not a list.
        TypeError: If the list contains elements that cannot be compared.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr

    # Perform insertion sort
    for i in range(1, len(arr)):
        # Store the current element to insert
        current = arr[i]
        
        # Find the correct position to insert the current element
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the current element in its correct position
        arr[j + 1] = current

    return arr