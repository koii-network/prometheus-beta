def select_kth_smallest(arr, k):
    """
    Implements the median of medians algorithm to find the kth smallest element in O(n) time.
    
    Args:
        arr (list): Input list of comparable elements
        k (int): The kth smallest element to find (1-based indexing)
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is out of bounds or input is invalid
    """
    if not arr or k < 1 or k > len(arr):
        raise ValueError("Invalid input: k must be within array bounds")
    
    return _select_kth(arr, 0, len(arr) - 1, k - 1)

def _select_kth(arr, left, right, k):
    """
    Recursive helper function for median of medians algorithm.
    
    Args:
        arr (list): Input list of comparable elements
        left (int): Left index of the current subarray
        right (int): Right index of the current subarray
        k (int): The kth smallest element to find (0-based indexing)
    
    Returns:
        The kth smallest element in the subarray
    """
    # If the subarray has few elements, use sorting
    if right - left < 5:
        sorted_subarray = sorted(arr[left:right+1])
        return sorted_subarray[k - left]
    
    # Divide the array into groups of 5 and find their medians
    num_groups = (right - left + 1) // 5
    medians = []
    
    for i in range(num_groups):
        group_start = left + i * 5
        group_median = _find_median(arr, group_start, group_start + 4)
        medians.append(group_median)
    
    # Handle remaining elements if array length is not divisible by 5
    if (right - left + 1) % 5 != 0:
        last_group_start = left + num_groups * 5
        last_group_median = _find_median(arr, last_group_start, right)
        medians.append(last_group_median)
    
    # Recursively find the median of medians
    pivot = _select_kth(medians, 0, len(medians) - 1, len(medians) // 2)
    
    # Partition the array around the pivot
    pivot_index = _partition(arr, left, right, pivot)
    
    # Recursively search the appropriate subarray
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return _select_kth(arr, left, pivot_index - 1, k)
    else:
        return _select_kth(arr, pivot_index + 1, right, k)

def _find_median(arr, start, end):
    """
    Find the median of a small subarray.
    
    Args:
        arr (list): Input list of comparable elements
        start (int): Start index of the subarray
        end (int): End index of the subarray
    
    Returns:
        The median of the subarray
    """
    sorted_subarray = sorted(arr[start:end+1])
    return sorted_subarray[len(sorted_subarray) // 2]

def _partition(arr, left, right, pivot):
    """
    Partition the array around a pivot value.
    
    Args:
        arr (list): Input list of comparable elements
        left (int): Left index of the current subarray
        right (int): Right index of the current subarray
        pivot (comparable): Pivot value to partition around
    
    Returns:
        The final index of the pivot
    """
    # Find the index of the pivot in the array
    pivot_index = arr.index(pivot, left, right + 1)
    
    # Swap pivot with the rightmost element
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    
    # Partition the array
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    
    # Put the pivot in its final place
    arr[right], arr[store_index] = arr[store_index], arr[right]
    
    return store_index