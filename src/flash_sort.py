def flash_sort(arr):
    """
    Implement the Flash Sort algorithm for efficient sorting.
    
    Flash Sort is a distribution sorting algorithm that works well for 
    uniformly distributed data. It has an average time complexity of O(n).
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list in ascending order
    """
    if not arr:
        return []
    
    # Find the minimum and maximum values
    min_val = min(arr)
    max_val = max(arr)
    
    # Handle the case where all elements are the same
    if min_val == max_val:
        return arr.copy()
    
    # Number of classes (buckets)
    m = int(0.43 * len(arr)) + 1
    
    # Initialize classes (buckets)
    L = [0] * m
    
    # Calculate the width of each class
    c1 = (m - 1) / (max_val - min_val)
    
    # Count the number of elements in each class
    for item in arr:
        j = int(c1 * (item - min_val))
        L[j] += 1
    
    # Accumulate the count to determine class boundaries
    for i in range(1, m):
        L[i] += L[i-1]
    
    # Perform the sorting
    sorted_arr = [0] * len(arr)
    
    # Redistribute the elements
    for i in range(len(arr) - 1, -1, -1):
        j = int(c1 * (arr[i] - min_val))
        sorted_arr[L[j] - 1] = arr[i]
        L[j] -= 1
    
    # Insertion sort on small classes (optimization)
    def insertion_sort(start, end):
        for i in range(start + 1, end + 1):
            key = sorted_arr[i]
            j = i - 1
            while j >= start and sorted_arr[j] > key:
                sorted_arr[j + 1] = sorted_arr[j]
                j -= 1
            sorted_arr[j + 1] = key
    
    # Sort small classes
    last = 0
    for i in range(m):
        if L[i] - last > 1:
            insertion_sort(last, L[i] - 1)
        last = L[i]
    
    return sorted_arr